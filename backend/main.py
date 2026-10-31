from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "HealthAI API работает"}


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "healthai-api"
    }