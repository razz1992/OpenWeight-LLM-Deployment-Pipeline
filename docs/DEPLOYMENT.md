# Container build, registry publishing, and smoke testing

## Delivery flow

1. GitHub Actions installs Python dependencies, compiles the API, and runs unit tests.
2. After tests pass, pushes to the default branch and manual workflow runs build the container.
3. The workflow authenticates with GitHub Container Registry using the built-in GITHUB_TOKEN.
4. The image is published to ghcr.io/<owner>/<repository> with a commit-SHA tag and, on the default branch, a latest tag.
5. A separate smoke-test job pulls the exact SHA-tagged image from GHCR.
6. The smoke test starts the container with model loading enabled, waits for /health to report model_loaded=true, and calls /generate.
7. Pull requests run tests and build the image but do not publish or run the GHCR smoke test.

## Model download and startup

The Docker image contains the API and Python dependencies, not model weights. The container downloads Hugging Face model files at startup using MODEL_ID and Transformers. The default model is HuggingFaceTB/SmolLM2-360M.

The Hugging Face cache is stored at /home/app/.cache/huggingface inside the container. It is ephemeral in the smoke-test job. A fresh container or deployment without persistent storage may download the weights again.

Optional configuration:
- MODEL_ID: Hugging Face model repository ID.
- MODEL_DEVICE: Transformers device selection. The smoke test sets this to cpu.
- LOAD_MODEL_ON_STARTUP: defaults to true in the container image. Set false for API-only checks.
- HF_HOME: Hugging Face cache directory.

For gated models, provide a Hugging Face token through a runtime secret such as HF_TOKEN. Do not bake tokens into the image or commit them.

## Smoke-test scope and limits

The GHCR smoke test validates image pull access, container startup, model download and load, the health response, and a real generation request on a GitHub-hosted CPU runner. It has a 30-minute job timeout and allows up to 15 minutes for model readiness.

This is a one-run integration check. It does not validate GPU behavior, production throughput, concurrency, persistent model caching, or AWS networking. A successful smoke test is not a production load test.

## Registry access

The workflow requires repository Actions permission to write packages. The image package may initially be private; configure package visibility in GitHub if public pulls are desired. No PAT is required by this workflow.

## Local verification without Docker

Docker is intentionally not required on the Windows machine. GitHub Actions is the authoritative container build and smoke-test environment. The Kaggle notebook remains the model experimentation environment.

## Cloud boundary

Publishing to GHCR and running the smoke test on GitHub-hosted runners does not provision AWS resources. AWS deployment requires a separate architecture and cost review plus explicit approval.
