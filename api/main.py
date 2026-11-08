import os
from fastapi import FastAPI, HTTPException
from api.schemas.generation import GenerateRequest, GenerateResponse
from api.services.model_service import ModelService

app = FastAPI(title="Open-Weight LLM API", version="0.1.0")
model_service = ModelService(model_id=os.getenv("MODEL_ID", "HuggingFaceTB/SmolLM2-360M"))

@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": model_service.generator is not None}

@app.post("/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest):
    try:
        output = model_service.generate(request.prompt, request.max_new_tokens, request.temperature)
        return GenerateResponse(model=model_service.model_id, generated_text=output)
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc))
