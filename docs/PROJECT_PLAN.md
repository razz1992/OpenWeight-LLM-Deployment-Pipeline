# Project Plan: Open-Weight LLM Deployment Pipeline

## Purpose
Build a reusable, on-demand pipeline demonstrating model acquisition, inference, optimization, API integration, container packaging, tests, CI/CD, AWS deployment concepts, monitoring and evaluation. This is a learning template, not an always-on service.

## Fixed constraints
| Constraint | Decision |
|---|---|
| Budget | ₹0 target; no paid resource without explicit approval |
| Duration | 15 working days |
| Models | Start around 360M–0.5B; progress to 1.5B–3B as resources allow |
| Model experiments | Kaggle |
| Local development | Windows + WSL2 Ubuntu |
| Local Docker | Do not install |
| Container builds | GitHub Actions hosted runner |
| Cloud | AWS; templates first, deployment only after approval and cost check |
| Hosting | No persistent API hosting |

## Execution architecture
1. Hugging Face: model cards, license review, IDs, revisions and downloads.
2. Kaggle: model loading, GPU inference, quantization and benchmarks.
3. WSL2: Python development, FastAPI and tests.
4. GitHub: source control, docs and configuration.
5. GitHub Actions: lint, tests and remote Docker image builds.
6. AWS CloudShell/console: AWS CLI and deployment learning, subject to feature and cost limits.
7. Monitoring: short-lived metrics collection and evaluation.

Kaggle sessions/GPU availability are quota-limited. CloudShell capabilities and persistence have limits. GitHub runner usage is subject to account allowances.

## Technology baseline
| Concern | Initial choice | Comparison |
|---|---|---|
| Model repository | Hugging Face Hub | Model cards and revisions |
| Framework | Transformers + PyTorch | Native model loading |
| Inference runtime | llama.cpp or Transformers, selected by model/format | Ollama |
| Quantized format | GGUF where supported | Other formats |
| API | FastAPI | Direct inference |
| Tests | pytest | Integration/evaluation scripts |
| Container | Dockerfile / Compose files | OCI image concepts |
| CI/CD | GitHub Actions | Manual workflow dispatch |
| Cloud | AWS ECR, ECS, EC2, IAM, VPC | — |
| IaC | CloudFormation | Template validation |
| Monitoring | Python metrics initially | Prometheus/Grafana |

## Model progression
- SmolLM2 360M: initial loading and inference.
- Qwen2.5 0.5B: API and serving.
- Qwen2.5 1.5B: optimization and quantization.
- Qwen2.5 3B: optional hosted-GPU experiment.

Verify availability, license, compatible format, revision and Kaggle resources before choosing a model. Do not assume all models have GGUF variants.

## 15-day roadmap
### Week 1 — Model engineering
| Day | Activity | Evidence |
|---|---|---|
| 1 | Verify Windows, WSL2, Ubuntu, Python, Git and Kaggle readiness | Environment report |
| 2 | Hugging Face, architecture, model files, tokenizer, license and revisions | Model selection notes |
| 3 | Load and run a small model in Kaggle | Notebook and output |
| 4 | Inference engines, generation settings and memory behavior | Inference notes |
| 5 | Quantization and benchmark design | Benchmark table |
| 6 | Compare Transformers, llama.cpp and Ollama | Comparison report |

### Week 2 — API and containers
| Day | Activity | Evidence |
|---|---|---|
| 7 | Design FastAPI inference service and schemas | API skeleton |
| 8 | Validation, errors, streaming design and tests | Passing tests |
| 9 | Dockerfile and Compose template; layers, volumes, health checks | Container files |
| 10 | Build and execute image remotely; inspect logs, tags and cleanup | Build log and notes |

### Week 3 — CI/CD, AWS and observability
| Day | Activity | Evidence |
|---|---|---|
| 11 | GitHub Actions linting and tests | CI workflow |
| 12 | Image build, tags and artifact handling | Build workflow |
| 13 | IAM, ECR, ECS, EC2, VPC and security groups | AWS architecture notes |
| 14 | CloudFormation and safe deployment workflow | Validated template |
| 15 | Metrics, evaluation, rollback concepts and documentation | Completion review |

Timeline is a learning target; quotas and troubleshooting may extend tasks.

## Acceptance criteria
- Run at least one open-weight model; record model ID, revision, license and configuration.
- Demonstrate generation and inference settings.
- Compare an optimization/quantization configuration where supported.
- Create FastAPI template and tests.
- Create Dockerfile and Compose templates without local Docker.
- Build an image on a remote GitHub Actions runner.
- Automate linting/tests.
- Produce AWS templates and explain deployment.
- Measure latency/resource use and evaluate outputs.
- Document execution and cleanup; exclude weights and secrets from Git.

## Cost and safety
- No EC2, ECS service, load balancer, NAT Gateway, SageMaker endpoint or paid GPU by default.
- AWS templates are not deployed unless explicitly approved.
- Before deployment, estimate region, duration, storage, networking and cleanup cost.
- Do not assume free-tier eligibility or quota.
- Stop and delete temporary resources after approved exercises.
- Do not redistribute weights unless license permits.
- Never store credentials in source files or notebook output.

## Procedure for each assignment
1. Explain concept and architectural role.
2. List prerequisites and cost.
3. Provide code/commands and explain parameters.
4. Execute in selected environment.
5. Verify using tests or observable evidence.
6. Record troubleshooting.
7. Update progress and learning log.
8. Ask before irreversible or potentially chargeable actions.

## Completion
The repository will be a reusable blueprint with independent model, inference, API, container, CI/CD, AWS and monitoring components. Individual stages can run on demand without an always-on service.
