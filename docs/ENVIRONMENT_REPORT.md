# Day 1 — Environment Inspection Report

**Inspection date:** 2026-11-08  
**Machine:** RAJNISH (Windows desktop)

## Verified environment

| Component | Finding | Assessment |
|---|---|---|
| OS | Windows 11 Home Single Language, build 26200, 64-bit | Supported host OS |
| CPU | AMD Ryzen 3 3250U, 2 cores / 4 logical processors | Suitable for development; CPU inference limited |
| RAM | 13.94 GB detected | Keep local workloads lightweight |
| GPU | AMD Radeon(TM) Graphics integrated GPU | Do not assume CUDA compatibility |
| Firmware virtualization | Enabled (True) | Hardware virtualization is available |
| WSL | Not installed (wsl --status confirms) | WSL2 setup remains pending |
| Python | 3.14 and 3.15 installed | Do not use these as project baseline yet |
| Git | 2.56.0.windows.4 | Available |
| GitHub CLI | 2.101.0, authenticated as razz1992 | Available |
| Kaggle CLI | Not installed / command not found | Not required for browser notebooks |
| Docker | Not detected | Consistent with no-local-Docker decision |
| NVIDIA CUDA tooling | Not detected | Use Kaggle GPU for CUDA experiments |

## Recommended setup decisions

1. Use WSL2 with Ubuntu for Linux-based development, after explicit approval to enable/install Windows components. This may require administrator privileges and a restart.
2. Use Python 3.12 inside Ubuntu as the initial compatibility baseline for the ML/API learning stack. Keep existing Windows Python 3.14/3.15 installations unchanged.
3. Use Kaggle in the browser for GPU notebooks. Install Kaggle CLI only if a later workflow needs programmatic notebook or dataset management.
4. Keep local model downloads small. Use Kaggle storage/session resources for model experiments and do not commit weights to Git.
5. Do not install Docker locally. Use GitHub Actions hosted runners for image builds.

## Blockers / approvals

- WSL2 and Ubuntu are not installed. Enabling Windows optional features requires elevation; no feature changes were attempted.
- User approval is required before enabling WSL2 / installing Ubuntu.
- Kaggle account and GPU accelerator availability have not yet been verified.

## Verification note

The Windows feature-state query was blocked because the current process is not elevated. The WSL command itself confirms that WSL is not installed. Firmware virtualization is enabled.
