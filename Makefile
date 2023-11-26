environment:
	@echo "Poetry is installing..."
	@poetry install
	@echo "Activating virtual environment..."
	@source venv/bin/activate
	@echo "Done."

.PHONY: environment