from fastapi import FastAPI
from app.api.users import router as users_router
from app.api.auth import router as auth_router
from app.api.tasks import router as tasks_router

# Create an instance of the FastAPI application
app = FastAPI(
    title="Task Tracker API",
    description="API for the task management system",
    version="1.0.0"
)

app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(auth_router, tags=["Auth"])
app.include_router(tasks_router, prefix="/tasks", tags=["Tasks"])

# Define the root endpoint
@app.get("/")
async def root():
    return {
        "status": "ok", 
        "message": "Hello! FastAPI is successfully running."
    }