CHECKFILES := setup.py
CHECKDIRS := src test


# run checks on all files for the repo
quality:
	@echo "Running python quality checks";
	black --check $(CHECKFILES) $(CHECKDIRS);
	isort --check-only $(CHECKFILES) $(CHECKDIRS);
	flake8 $(CHECKFILES) $(CHECKDIRS);
	mypy $(CHECKDIRS);

# style the code according to accepted standards for the repo
style:
	pre-commit run --all-files -c .pre-commit-config.yaml
