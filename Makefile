environment:
	@echo "Setting up the environment..."
	@uv venv --python 3.12 --clear
	@echo "Virtual environment created in .venv"
	@echo "Activate it with: source .venv/bin/activate"
	@echo "Or use: uv run main.py (no need to activate manually)"
	@echo "Then run: make install"
.PHONY: environment

# Adicionar novos targets para usar uv
install:
	@echo "Installing dependencies with uv..."
	@uv pip install -e .

install-dev:
	@echo "Installing development dependencies with uv..."
	@uv pip install -e ".[dev]"

update:
	@echo "Updating dependencies with uv..."
	@uv pip install --upgrade -e .

activate:
	@echo "To activate the virtual environment, run:"
	@echo "source venv/bin/activate"

clean:
	@echo "Cleaning up..."
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info/
	@find . -type d -name __pycache__ -delete
	@find . -type f -name "*.pyc" -delete

clean-env:
	@echo "Removing virtual environment..."
	@rm -rf .venv/

.PHONY: install install-dev update activate clean clean-env