from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from celery.result import AsyncResult
from celery.exceptions import TimeoutError
from app.worker import run_optimization_task
import logging

# Configure logger
logger = logging.getLogger(__name__)
router = APIRouter()

class OptimizationRequest(BaseModel):
    iterations: int = 1000
    temperature: float = 100.0
    cooling_rate: float = 0.95
    function: str = "rastrigin"

@router.post("/optimize", status_code=status.HTTP_202_ACCEPTED)
def start_optimization(request: OptimizationRequest):
    """
    Start a background optimization task.
    """
    try:
        task = run_optimization_task.delay(
            iterations=request.iterations,
            temp=request.temperature,
            cooling_rate=request.cooling_rate,
            function_name=request.function
        )
        return {"task_id": task.id, "status": "Processing"}
    except Exception as e:
        logger.error(f"Failed to queue task: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Could not submit optimization task. Verify Redis is running."
        )

@router.get("/tasks/{task_id}")
def get_task_status(task_id: str):
    """
    Get the status of a specific task.
    """
    try:
        task_result = AsyncResult(task_id)
        if not task_result:
             raise HTTPException(status_code=404, detail="Task not found")
             
        return {
            "task_id": task_id,
            "status": task_result.status,
            "result": task_result.result if task_result.ready() else None
        }
    except Exception as e:
        logger.error(f"Error checking task status: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
