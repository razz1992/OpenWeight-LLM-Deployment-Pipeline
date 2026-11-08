import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException

from api.schemas.generation import GenerateRequest, GenerateResponse
from api.services.model_service import ModelService


model_service = ModelService(model_id=os.getenv("MODEL_ID", "HuggingFaceTB/SmolLM2-360M"))


@asynccontextmanager
async def lifespan(_: FastAPI):
    """Load model weights at container startup when explicitly enabled."""
    if os.getenv("LOAD_MODEL_ON_STARTUP", "false").lower() in {"1", "true", "yes"}:
        model_service.load(device=os.getenv("MODEL_DEVICE", "auto"))
    yield


app = FastAPI(
    title="Open-Weight LLM API",
    version="0.2.0",
    lifespan=lifespan,
)


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": model_service.generator is not None}


@app.post("/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest):
    try:
        output = model_service.generate(
            request.prompt, request.max_new_tokens, request.temperature
        )
        return GenerateResponse(model=model_service.model_id, generated_text=output)
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc))
