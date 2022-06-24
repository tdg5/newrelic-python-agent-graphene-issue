CHECKGLOBS := 'src/**/*.py' 'utils/**/*.py' setup.py
DOCDIR := docs
CHECKDIRS := src utils setup.py


# run checks on all files for the repo
quality:
	@echo "Running copyright checks";
	python utils/copyright.py quality $(CHECKGLOBS) $(MDCHECKGLOBS)
	@echo "Running python quality checks";
	black --check $(CHECKDIRS);
	isort --check-only $(CHECKDIRS);
	flake8 $(CHECKDIRS);

# style the code according to accepted standards for the repo
style:
	@echo "Running copyrighting";
	python utils/copyright.py style $(CHECKGLOBS) $(MDCHECKGLOBS) 
	@echo "Running python styling";
	black $(CHECKDIRS);
	isort $(CHECKDIRS);