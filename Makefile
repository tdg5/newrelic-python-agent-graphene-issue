CHECKGLOBS := setup.py 'src/**/*.py' 'test/**/*.py'
DOCDIR := docs
CHECKDIRS := setup.py src test


# run checks on all files for the repo
quality:
	@echo "Running python quality checks";
	black --check $(CHECKDIRS);
	isort --check-only $(CHECKDIRS);
	flake8 $(CHECKDIRS);

# style the code according to accepted standards for the repo
style:
	@echo "Running python styling";
	black $(CHECKDIRS);
	isort $(CHECKDIRS);
