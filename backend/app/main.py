from fastapi import FastAPI

app = FastAPI(
    title="CloudWise AI API",
    description="Backend API for the CloudWise AI AWS Solution Advisor.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "cloudwise-ai-backend",
        "version": "0.1.0",
    }