from fastapi import APIRouter
from app.schemas import JobRequest

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)

# Global in-memory storage
last_job = {"task": None}


@router.post("/run")
def run_job(data: JobRequest):
    last_job["task"] = data.task
    print(f"Job triggered: {data.task}")
    return {
        "message": "Job triggered successfully",
        "task": data.task
    }


@router.get("/status")
def get_job_status():
    print("STATUS CHECK:", last_job)
    if last_job["task"] is None:
        return {"status": "No job has been triggered yet"}
    return {
        "status": "Last job triggered",
        "task": last_job["task"]
    }

