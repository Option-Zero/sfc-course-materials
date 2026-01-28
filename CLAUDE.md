# Claude Code Instructions

## Python Environment: UV

This project uses [UV](https://docs.astral.sh/uv/) for Python package management.

### Adding Dependencies

Use `uv add` to add dependencies (NOT `uv pip install`):

```bash
# Add a package
uv add package-name

# Add a dev dependency
uv add --dev package-name
```

### Running Scripts

Use `uv run` to execute Python scripts:

```bash
# Run a script
uv run python script.py

# Run a module
uv run python -m module_name
```

### Why UV?

- `uv add` updates pyproject.toml and creates/updates uv.lock for reproducibility
- `uv run` ensures the correct virtual environment is used automatically
- Faster than pip for dependency resolution
