import numpy as np
import asyncio

async def genetic_algorithm_search(func_impl, dim: int, bounds: tuple, pop_size=50, generations=20):
    """
    Executes a Genetic Algorithm to explore the solution space and find a promising 
    basin of attraction.
    
    Args:
        func_impl (callable): The objective function to minimize.
        dim (int): Number of dimensions.
        bounds (tuple): (min, max) for each dimension.
        pop_size (int): Population size.
        generations (int): Number of generations to evolve.
        
    Returns:
        np.ndarray: The best solution vector found.
    """
    # Initialize population: [pop_size, dim] containing random values within bounds
    population = np.random.uniform(bounds[0], bounds[1], (pop_size, dim))
    
    # Evaluate initial population
    best_sol = population[0]
    best_score = func_impl(best_sol)
    
    for _ in range(generations):
        # 1. Evaluation
        scores = np.array([func_impl(ind) for ind in population])
        
        # 2. Elitism: Keep the best found so far
        min_idx = np.argmin(scores)
        if scores[min_idx] < best_score:
            best_score = scores[min_idx]
            best_sol = population[min_idx]

        # 3. Selection & Reproduction (Tournament logic simplified)
        next_pop = []
        for _ in range(pop_size):
            # Tournament Selection: Pick 2 random parents
            p1 = population[np.random.randint(pop_size)]
            p2 = population[np.random.randint(pop_size)]
            
            # Crossover: Uniform Crossover
            mask = np.random.rand(dim) > 0.5
            child = np.where(mask, p1, p2)
            
            # Mutation: Gaussian perturbation with 20% probability
            if np.random.rand() < 0.2:
                mutation_strength = 0.1 * (bounds[1] - bounds[0]) # Dynamic based on scale
                child += np.random.normal(0, mutation_strength * 0.1, dim)
                child = np.clip(child, bounds[0], bounds[1])
            
            next_pop.append(child)
            
        population = np.array(next_pop)
        
    return best_sol
