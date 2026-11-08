# Open-Weight LLM Deployment Pipeline

Reusable, on-demand learning project for the lifecycle of deploying open-weight language models.

## Execution strategy
- Kaggle Notebooks: primary execution environment for model experiments and GPU inference.
- GitHub Actions: Python tests, remote Docker image build and GHCR publishing.
- GHCR: stores the API container image; model weights are downloaded at container startup and are not baked into the image.
- AWS: future deployment target; no chargeable provisioning without explicit approval.
- No WSL2, Ubuntu installation, local Docker installation, persistent hosting or paid cloud resources.

## Quick start in Kaggle
1. Open notebooks/kaggle_end_to_end_pipeline.ipynb from the repository or import it into Kaggle.
2. Select a GPU accelerator only if available; enable Internet for model download.
3. Run cells in order. The notebook clones this repository, installs dependencies, runs API tests, loads the configured model, performs inference, records latency/memory and saves a JSON report.
4. Kaggle sessions and GPU quotas are limited. Use the CPU path for API/unit tests if no GPU is available.

## Pipeline stages
1. Model and license metadata review.
2. Hugging Face model download and tokenizer/model loading.
3. Text generation and inference benchmark.
4. FastAPI health/generation API and pytest validation.
5. Docker image build on GitHub-hosted runners.
6. Publish the image to GHCR after tests pass; pull requests build without publishing.
7. Future AWS deployment after separate architecture, cost review and explicit approval.

## Container runtime configuration
- MODEL_ID defaults to HuggingFaceTB/SmolLM2-360M.
- LOAD_MODEL_ON_STARTUP defaults to true in the container.
- MODEL_DEVICE defaults to auto.
- HF_HOME defaults to /home/app/.cache/huggingface.
- Model files are downloaded at container startup and cached inside the container. Without a persistent volume, a replacement container may download them again.

See docs/DEPLOYMENT.md, docs/PROJECT_PLAN.md, docs/DECISIONS.md and docs/PROGRESS.md.

## Constraints
- Budget target: ₹0 additional spend.
- Never commit model weights, datasets, credentials, tokens or private keys.
- Do not redistribute model weights unless the model license permits it.
- Container builds and registry publishing happen on GitHub-hosted runners, not locally.
- AWS resources are not provisioned without explicit approval and a cost check.
