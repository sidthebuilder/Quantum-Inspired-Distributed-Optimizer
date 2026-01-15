import numpy as np
import math
import time

def objective_function(x):
    """
    Rastrigin function - a standard test function for optimization algorithms.
    Global minimum at x = 0 with value 0.
    """
    A = 10
    return A * len(x) + sum([(xi**2 - A * np.cos(2 * math.pi * xi)) for xi in x])

async def simulated_annealing(
    dim: int = 10,
    bounds: tuple = (-5.12, 5.12),
    iterations: int = 1000,
    temp: float = 100.0,
    cooling_rate: float = 0.95
):
    """
    Simulates a quantum annealing process (classically) to minimize the objective function.
    Returns the track of the optimization for visualization.
    """
    # 1. Initialize State
    current_solution = np.random.uniform(bounds[0], bounds[1], dim)
    current_energy = objective_function(current_solution)
    
    best_solution = current_solution.copy()
    best_energy = current_energy
    
    history = []

    # 2. Annealing Loop
    for i in range(iterations):
        # Create candidate solution (perturbation)
        candidate_solution = current_solution + np.random.uniform(-0.5, 0.5, dim)
        candidate_solution = np.clip(candidate_solution, bounds[0], bounds[1])
        candidate_energy = objective_function(candidate_solution)
        
        # Calculate energy delta
        delta_energy = candidate_energy - current_energy
        
        # Acceptance probability (Metropolis criterion)
        acceptance_prob = 1.0 if delta_energy < 0 else math.exp(-delta_energy / temp)
        
        # Decide to accept
        if np.random.rand() < acceptance_prob:
            current_solution = candidate_solution
            current_energy = candidate_energy
            
            # Update best found
            if current_energy < best_energy:
                best_solution = current_solution
                best_energy = current_energy
        
        # Record state for visualization (store only 2D projection or summary for simpler UI)
        history.append({
            "step": i,
            "energy": float(current_energy),
            "temp": float(temp),
            "best_energy": float(best_energy),
            "coordinates": current_solution[:2].tolist() # sending first 2 dims for 2D plot
        })
        
        # Cool down
        temp *= cooling_rate
        
    return {
        "final_solution": best_solution.tolist(),
        "final_energy": float(best_energy),
        "history": history
    }
