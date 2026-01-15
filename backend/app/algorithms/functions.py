import numpy as np
import math

def rastrigin(x):
    """
    Rastrigin function (Multi-modal).
    Global minimum at 0, value 0.
    Range: [-5.12, 5.12]
    """
    A = 10
    return A * len(x) + sum([(xi**2 - A * np.cos(2 * math.pi * xi)) for xi in x])

def sphere(x):
    """
    Sphere function (Convex).
    Global minimum at 0, value 0.
    Range: [-infinity, infinity]
    """
    return sum([xi**2 for xi in x])

def rosenbrock(x):
    """
    Rosenbrock function (Valley).
    Global minimum at (1,1,...), value 0.
    Range: [-5, 10] usually.
    """
    return sum([100.0*(x[i+1] - x[i]**2)**2 + (1 - x[i])**2 for i in range(len(x)-1)])

FUNCTIONS = {
    "rastrigin": {
        "func": rastrigin,
        "bounds": (-5.12, 5.12),
        "desc": "Rugged landscape with many local minima."
    },
    "sphere": {
        "func": sphere,
        "bounds": (-10.0, 10.0),
        "desc": "Simple bowl shape, easy to optimize."
    },
    "rosenbrock": {
        "func": rosenbrock,
        "bounds": (-2.048, 2.048), # Standard testing range
        "desc": "Narrow valley, hard to converge exactly."
    }
}

def get_function(name: str):
    return FUNCTIONS.get(name.lower(), FUNCTIONS["rastrigin"])
