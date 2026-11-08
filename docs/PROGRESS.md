# Project Progress

**Current phase:** Container delivery and runtime validation
**Current task:** Verify the GHCR-published image with a real model-load and inference smoke test.

## Completed
- [x] Create local project scaffold and public GitHub repository.
- [x] Build the FastAPI inference API and unit tests.
- [x] Prepare the Kaggle end-to-end notebook and record baseline validation results.
- [x] User confirmed GHCR as registry, AWS later, and runtime model download.
- [x] Add container startup model loading controlled by LOAD_MODEL_ON_STARTUP.
- [x] Configure Docker image with CPU-only PyTorch, non-root runtime user and health check.
- [x] Configure GitHub Actions to run tests, build on pull requests without publishing, and publish on main/manual runs.
- [x] Publish the container to GHCR with latest and commit-SHA tags.
- [x] Add a GHCR smoke-test job that pulls the SHA image, loads SmolLM2-360M on CPU, verifies /health reports model_loaded=true, and calls /generate.
- [x] Document smoke-test scope, timeout, and limitations.

## Validation status
- Previous CI test and container publication passed in workflow run #7.
- The new smoke-test workflow has been added but has not yet run.
- git diff --check passed for the workflow and deployment documentation.
- Local YAML parsing is unavailable because PyYAML is not installed; GitHub Actions will validate the workflow on push.
- Docker is intentionally not installed or used on the Windows machine.
- No AWS resources have been provisioned.

## Next checks
- [ ] Push the smoke-test workflow and documentation changes.
- [ ] Confirm unit tests and container build/publish jobs pass.
- [ ] Confirm the published image pulls, the model loads, /health reports model_loaded=true, and /generate returns non-empty text.
- [ ] Diagnose any model download, startup, memory, or inference failures before AWS planning.
- [ ] Plan AWS deployment only after separate approval and cost review.

## Constraints
- No WSL2 or Ubuntu installation.
- No local Docker installation.
- No AWS resources or paid cloud infrastructure without explicit approval.
- Model weights and credentials must not be committed to the repository.
