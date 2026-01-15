import pytest
import numpy as np
from app.algorithms.annealing import simulated_annealing, objective_function

@pytest.mark.asyncio
async def test_simulated_annealing_improves_energy():
    """
    Test that the annealing process actually reduces the objective function (energy).
    Rastrigin global minimum is 0.
    """
    result = await simulated_annealing(
        dim=2,
        iterations=1000,
        temp=100.0,
        cooling_rate=0.9
    )
    
    assert "final_energy" in result
    assert "history" in result
    
    # Check if we improved over the run (usually start is much higher than end)
    initial_energy = result['history'][0]['energy']
    final_energy = result['final_energy']
    
    # Annealing should almost always improve from a random start
    assert final_energy <= initial_energy

def test_objective_function_at_zero():
    """
    Test that the objective function returns 0 at x=[0,0...].
    """
    zero_point = np.zeros(5)
    energy = objective_function(zero_point)
    assert energy == 0.0

def test_objective_function_positive():
    """
    Rastrigin function should be positive everywhere (or 0).
    """
    random_point = np.random.uniform(-5, 5, 5)
    energy = objective_function(random_point)
    assert energy >= 0.0
