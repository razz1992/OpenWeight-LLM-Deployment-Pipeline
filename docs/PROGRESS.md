# Project Progress

**Current phase:** Container delivery pipeline
**Current task:** Validate CI, build the Docker image and publish it to GHCR.

## Completed
- [x] Create local project scaffold and public GitHub repository.
- [x] Build the FastAPI inference API and unit tests.
- [x] Prepare the Kaggle end-to-end notebook and record baseline validation results.
- [x] User confirmed GHCR as registry, AWS later, and runtime model download.
- [x] Add container startup model loading controlled by LOAD_MODEL_ON_STARTUP.
- [x] Configure Docker image with CPU-only PyTorch, non-root runtime user and health check.
- [x] Configure GitHub Actions to run tests, build on pull requests without publishing, and publish on main/manual runs.
- [x] Document container runtime configuration and delivery process.

## Validation status
- Python source compilation passed locally.
- git diff --check passed after whitespace cleanup.
- Local pytest could not run because pytest is not installed in the Windows Python environment; no global packages were installed.
- Local YAML parsing could not run because PyYAML is not installed. GitHub Actions will validate the workflow on push.
- Docker build has not yet been run locally; local Docker installation remains intentionally out of scope.
- GHCR publication is not yet confirmed; it requires a successful GitHub Actions run.

## Next checks
- [ ] Push implementation and inspect GitHub Actions result.
- [ ] Confirm GHCR image tags were published.
- [ ] Review image package visibility and pull instructions.
- [ ] Run a container smoke test in a supported remote environment.
- [ ] Plan AWS deployment only after separate approval and cost review.

## Constraints
- No WSL2 or Ubuntu installation.
- No local Docker installation.
- No AWS resources or paid cloud infrastructure without explicit approval.
- Model weights and credentials must not be committed to the repository.
