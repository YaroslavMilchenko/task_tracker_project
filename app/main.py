from fastapi import FastAPI

# Create an instance of the FastAPI application
app = FastAPI(
    title="Task Tracker API",
    description="API for the task management system",
    version="1.0.0"
)

# Define the root endpoint
@app.get("/")
async def root():
    return {
        "status": "ok", 
        "message": "Hello! FastAPI is successfully running."
    }