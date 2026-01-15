from celery import Celery
from app.core.config import settings
import asyncio
from app.algorithms.annealing import simulated_annealing

celery_app = Celery("worker", broker=settings.REDIS_URL, backend=settings.REDIS_URL)

@celery_app.task(bind=True)
def run_optimization_task(self, iterations: int, temp: float, cooling_rate: float, function_name: str = "rastrigin"):
    # Using the new Hybrid Solver for better results
    from app.algorithms.hybrid import hybrid_optimization
    results = asyncio.run(hybrid_optimization(
        function_name=function_name,
        iterations=iterations,
        temp=temp,
        cooling_rate=cooling_rate
    ))
    return results
