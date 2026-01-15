import numpy as np
import asyncio
from .functions import get_function
from .genetic import genetic_algorithm_search

async def hybrid_optimization(
    function_name: str = "rastrigin",
    dim: int = 10,
    iterations: int = 1000,
    temp: float = 100.0,
    cooling_rate: float = 0.95
):
    """
    Orchestrates a Hybrid optimization strategy:
    1. Exploration: Genetic Algorithm finds a good starting point.
    2. Exploitation: Simulated Annealing refines the solution locally.
    """
    # 1. Configuration Check
    func_config = get_function(function_name)
    func_impl = func_config["func"]
    bounds = func_config["bounds"]
    
    # 2. Phase 1: Genetic Exploration
    # We use a small generation count just to get near a global minima basin
    ga_best_sol = await genetic_algorithm_search(func_impl, dim, bounds, pop_size=40, generations=15)
    
    # 3. Phase 2: Simulated Annealing (Exploitation)
    current_solution = ga_best_sol.copy()
    current_energy = func_impl(current_solution)
    
    best_solution = current_solution.copy()
    best_energy = current_energy
    
    history = []
    
    # Annealing Loop
    for i in range(iterations):
        # Generate candidate: Gaussian perturbation
        candidate_solution = current_solution + np.random.uniform(-0.5, 0.5, dim)
        candidate_solution = np.clip(candidate_solution, bounds[0], bounds[1])
        candidate_energy = func_impl(candidate_solution)
        
        # Metropolis Criterion
        delta_energy = candidate_energy - current_energy
        
        # Accept if better OR with probability exp(-delta/T)
        if delta_energy < 0 or np.random.rand() < np.exp(-delta_energy / temp):
            current_solution = candidate_solution
            current_energy = candidate_energy
            
            if current_energy < best_energy:
                best_solution = current_solution
                best_energy = current_energy
        
        # Telemetry
        history.append({
            "step": i,
            "energy": float(current_energy),
            "temp": float(temp),
            "best_energy": float(best_energy),
            "coordinates": current_solution[:2].tolist() # Capture 2D projection
        })
        
        # Cooling Schedule
        temp *= cooling_rate
        
    return {
        "final_solution": best_solution.tolist(),
        "final_energy": float(best_energy),
        "history": history,
        "method": f"Hybrid-GA-SA ({function_name})",
        "dimensions": dim
    }
