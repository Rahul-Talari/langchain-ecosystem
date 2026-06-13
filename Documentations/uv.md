# uv (Python Package Manager)
https://docs.astral.sh/uv/

## Definition
uv is a fast, modern Python package and project manager that handles  
dependencies, virtual environments, and reproducible builds in a unified workflow.

## Advantages
1. **Unified Tooling**: Replaces pip + venv with a single tool  
2. **Clean Dependency Management**: Keeps dependencies consistent and avoids conflicts  
3. **Reproducibility**: Uses `uv.lock` to ensure consistent environments  
4. **Automatic Environment Handling**: No need to manually activate virtual environments (via `uv run`)  
5. **High Performance**: 10–100x faster than pip (Rust-based)  

## Installation
```bash
pip install uv
```

### Project Setup
```bash
uv init <project-name>                # Initialize a new project
uv venv                               # Create virtual environment
.venv\Scripts\activate               Activate virtual environment
```

### Dependency Management
```bash
uv add <package1> <package2>          # Add dependencies
uv remove <package-name>              # Remove dependency
uv lock --upgrade                     # Update dependencies
uv sync                               # Install from uv.lock
uv tree                               # View dependency tree
```

### Execution
```bash
uv run main.py
# Runs script using project virtual environment
# Auto-syncs dependencies if required
```

## Add Dependencies Flow
1. Updates `pyproject.toml` → adds the dependency (what you want)
2. Resolves dependencies → finds compatible versions (+ sub-dependencies)
3. Updates `uv.lock` → stores exact versions (reproducibility)
4. Syncs environment → installs packages in `.venv`