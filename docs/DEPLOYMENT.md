# Container build and registry publishing

## Current delivery flow

1. GitHub Actions installs Python dependencies, compiles the API and runs unit tests.
2. After tests pass, pushes to the default branch and manual workflow runs build the container.
3. The workflow authenticates with GitHub Container Registry using the built-in GITHUB_TOKEN.
4. The image is published to ghcr.io/<owner>/<repository> with a commit-SHA tag and, on the default branch, a latest tag.
5. Pull requests run tests but do not publish an image.

## Model download and startup

The Docker image contains the API and Python dependencies, not model weights. The container downloads Hugging Face model files at startup using MODEL_ID and Transformers. The default model is HuggingFaceTB/SmolLM2-360M.

The Hugging Face cache is stored at /home/app/.cache/huggingface inside the container. It is ephemeral unless a future deployment mounts persistent storage. A restart without persistent storage may download the weights again.

Optional configuration:
- MODEL_ID: Hugging Face model repository ID.
- MODEL_DEVICE: Transformers device selection; defaults to auto.
- LOAD_MODEL_ON_STARTUP: defaults to true in the container image. Set false for tests or API-only checks.
- HF_HOME: Hugging Face cache directory.

For gated models, provide a Hugging Face token through a runtime secret such as HF_TOKEN. Do not bake tokens into the image or commit them.

## Registry access

The workflow requires repository Actions permission to write packages. The image package may initially be private; configure package visibility in GitHub if public pulls are desired. No PAT is required by this workflow.

## Local verification without Docker

Docker is intentionally not required on the Windows machine. GitHub Actions is the authoritative container build environment. The Kaggle notebook remains the model experimentation environment.

## Cloud boundary

Publishing to GHCR is the current delivery target. No AWS resources are provisioned by this workflow. AWS deployment requires a separate architecture and cost review plus explicit approval.
