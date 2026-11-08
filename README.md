# Open-Weight LLM Deployment Pipeline

Reusable, on-demand learning project for the lifecycle of deploying open-weight language models.

## Constraints
- Budget target: ₹0 additional spend. Check current quotas/pricing before hosted resources.
- Timeline: 15 working days (2–3 weeks).
- Kaggle Notebooks for model/GPU experiments (quota-limited).
- Windows + WSL2 Ubuntu for development.
- No local Docker installation; container builds use GitHub Actions hosted runners.
- AWS is the target deployment platform; no chargeable provisioning without explicit approval.
- No persistent API hosting; start, test, stop and preserve reusable templates.

## Progress
- [x] Initial scaffold created.
- [ ] Day 1 environment verification.
- [ ] Model inference and benchmarking.
- [ ] FastAPI and tests.
- [ ] Remote container build.
- [ ] GitHub Actions CI/CD.
- [ ] AWS templates.
- [ ] Monitoring and evaluation.

See `docs/PROJECT_PLAN.md`, `docs/DECISIONS.md` and `docs/PROGRESS.md`.

Do not commit model weights, datasets, credentials, tokens or private keys.
