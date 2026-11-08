# Architecture Decisions

| ID | Decision | Rationale | Status |
|---|---|---|---|
| D-001 | Learning project, not production hosting | Avoid always-on operations | Accepted |
| D-002 | ₹0 additional-spend target | User constraint | Accepted |
| D-003 | No Docker on Windows or WSL2 | User constraint | Accepted |
| D-004 | Kaggle for GPU/model experiments | Local GPU is limited; Kaggle quota applies | Accepted |
| D-005 | Windows-first local workflow | No WSL2/Ubuntu installation | Accepted |
| D-006 | GitHub for source control | User-selected | Accepted |
| D-007 | GitHub Actions hosted runners for image builds | No local Docker engine | Accepted |
| D-008 | AWS as future deployment target | User-selected; deployment deferred | Accepted |
| D-009 | No persistent API hosting | User clarification | Accepted |
| D-010 | No paid AWS provisioning without approval | Preserve budget constraint | Accepted |
| D-011 | Start small, progress gradually | Hardware and learning constraints | Accepted |
| D-012 | Store references/configuration, not weights | Avoid binaries and licensing issues | Accepted |
| D-013 | Publish container images to GHCR after successful CI | User-approved registry choice | Accepted |
| D-014 | Download model weights from Hugging Face at container startup | Keep model weights out of the image | Accepted |
| D-015 | Do not provision AWS until separately approved | Avoid unplanned cloud costs | Accepted |

## Current delivery decisions

- Registry: GitHub Container Registry (ghcr.io).
- Image tags: latest on the default branch and immutable commit-SHA tags.
- Pull requests: test and build the image without publishing it.
- Main-branch pushes and manual workflow runs: publish after tests pass.
- Model: HuggingFaceTB/SmolLM2-360M by default; configurable through MODEL_ID.
- Model weights: downloaded at container startup; not included in the image.
- Hugging Face cache: container-local unless a future deployment mounts persistent storage.
- AWS: later phase only; no infrastructure provisioning in this step.
