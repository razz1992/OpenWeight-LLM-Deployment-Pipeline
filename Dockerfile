FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    MODEL_ID=HuggingFaceTB/SmolLM2-360M \
    LOAD_MODEL_ON_STARTUP=true \
    MODEL_DEVICE=auto \
    HF_HOME=/home/app/.cache/huggingface

WORKDIR /app

RUN useradd --create-home --uid 10001 app

COPY requirements.txt .
# Install CPU-only PyTorch so the image does not pull CUDA runtime packages.
RUN pip install --no-cache-dir --index-url https://download.pytorch.org/whl/cpu torch \
    && pip install --no-cache-dir -r requirements.txt

COPY --chown=app:app api ./api

RUN mkdir -p /home/app/.cache/huggingface && chown -R app:app /home/app

USER app

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=180s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=3)"

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
