# Project Plan: Open-Weight LLM Deployment Pipeline

## Purpose
Build a reusable, on-demand pipeline demonstrating model acquisition, inference, optimization, API integration, container packaging, tests, CI/CD, AWS deployment concepts, monitoring and evaluation.

## Fixed decisions
| Concern | Decision |
|---|---|
| Budget | ₹0 target; no paid resource without explicit approval |
| Runtime | Kaggle Notebooks for model experiments, inference, API and evaluation |
| Local machine | Windows only; no WSL2 or Ubuntu installation |
| Local Docker | Do not install |
| Container build | GitHub Actions hosted runner; build only, no registry push by default |
| Cloud | AWS templates first; no deployment without approval and cost check |
| Hosting | No persistent API hosting |

## Pipeline architecture
1. Hugging Face: model card, license, model ID, revision and download.
2. Kaggle: model loading, inference, benchmark, API tests and evaluation.
3. GitHub: source control, notebook, docs and configuration.
4. GitHub Actions: Python tests and remote OCI/Docker image build.
5. AWS: IAM/ECR/ECS/EC2/VPC and CloudFormation learning; templates only until approved.
6. Monitoring: latency, memory, generation quality smoke checks and run report.

Kaggle GPU availability and session duration are quota-limited. If GPU is unavailable, run API/unit tests on CPU and defer larger model benchmarks.

## Technology baseline
- Model: HuggingFaceTB/SmolLM2-360M as first smoke-test model; verify license and current model card.
- Framework: PyTorch + Transformers.
- API: FastAPI + Pydantic.
- Tests: pytest + FastAPI TestClient.
- Container: Dockerfile; build on GitHub-hosted runner.
- CI/CD: GitHub Actions; tests and build only, no push by default.
- Cloud: AWS templates and cost analysis only.

## Acceptance criteria
- Record model ID, revision and license metadata.
- Load at least one open-weight model and generate text.
- Record model load time, inference latency and available memory telemetry.
- Exercise FastAPI health and generation endpoints.
- Pass API unit and validation tests.
- Record whether quantization capability is available; run a quantized comparison only when supported.
- Build an OCI image on a GitHub-hosted runner.
- Document AWS architecture without provisioning chargeable resources.
- Save a reproducible JSON execution report.

## Pipeline boundary
Kaggle is used for Python/model/API execution. It is not the container build target because hosted notebook environments do not provide a supported privileged Docker daemon. GitHub Actions performs the image build. AWS deployment remains out of scope unless separately approved.

## Cost and safety
- No EC2, ECS service, load balancer, NAT Gateway, SageMaker endpoint or paid GPU by default.
- No registry push or AWS provisioning without explicit approval.
- Do not commit weights, datasets, tokens, credentials or private keys.
- Do not redistribute model weights unless license permits it.
- Stop and clean temporary resources after any separately approved exercise.
