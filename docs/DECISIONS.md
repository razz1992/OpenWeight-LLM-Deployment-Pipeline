# Architecture Decisions

| ID | Decision | Rationale | Status |
|---|---|---|---|
| D-001 | Learning project, not production hosting | Avoid always-on operations | Accepted |
| D-002 | ₹0 additional-spend target | User constraint | Accepted |
| D-003 | No Docker on Windows or WSL2 | User constraint | Accepted |
| D-004 | Kaggle for GPU/model experiments | Local GPU is limited; Kaggle quota applies | Accepted |
| D-005 | WSL2 Ubuntu for Python development | User-selected | Accepted |
| D-006 | GitHub for source control | User-selected | Accepted |
| D-007 | GitHub Actions hosted runners for image builds | No local Docker engine | Accepted |
| D-008 | AWS as deployment target | User-selected | Accepted |
| D-009 | No persistent API hosting | User clarification | Accepted |
| D-010 | No paid AWS provisioning without approval | Preserve budget constraint | Accepted |
| D-011 | Start small, progress gradually | Hardware and learning constraints | Accepted |
| D-012 | Store references/configuration, not weights | Avoid binaries and licensing issues | Accepted |

## Decisions to confirm
- GitHub destination: new repository `OpenWeight-LLM-Deployment-Pipeline` or existing repository.
- Visibility: public or private.
- Default branch: recommend `main`.
- WSL2: inspect current installation first; do not install/enable without approval.
