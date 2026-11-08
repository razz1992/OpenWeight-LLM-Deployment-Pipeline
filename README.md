# Open-Weight LLM Deployment Pipeline

Reusable, on-demand learning project for the lifecycle of deploying open-weight language models.

## Execution strategy
- Kaggle Notebooks: primary execution environment for model download, GPU inference, benchmarking, API tests and evaluation.
- GitHub Actions: remote Docker image build and CI checks (Kaggle does not provide a supported privileged Docker daemon).
- AWS: infrastructure templates and deployment learning only; no chargeable provisioning without explicit approval.
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
4. Optional quantization/low-memory experiment where runtime support permits.
5. FastAPI health/generation endpoint and pytest validation.
6. Evaluation smoke test and run report.
7. GitHub Actions remote container build; AWS templates remain non-deployed.

## Constraints
- Budget target: ₹0 additional spend.
- Never commit model weights, datasets, credentials, tokens or private keys.
- Do not redistribute model weights unless the model license permits it.
- Container builds happen on GitHub-hosted runners, not inside Kaggle.
- AWS resources are not provisioned without explicit approval and a cost check.

See docs/PROJECT_PLAN.md, docs/DECISIONS.md and docs/PROGRESS.md.
