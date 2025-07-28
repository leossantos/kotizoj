environment:
	@echo "Setting up the environment..."
	@pyenv install 3.13.5
	@pyenv virtualenv 3.13.5 kotizoj
	@pyenv local kotizoj
	@pip install --upgrade pip
	@pip install -e .
.PHONY: environment