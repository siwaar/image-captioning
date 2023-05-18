UPGRADE_PIP=yes
dir=image_captioning
ifeq ($(OS),Windows_NT)
	VENV=wenv
	PYTHON=.\$(VENV)\Scripts\python.exe
	SAFETY=.\$(VENV)\Scripts\safety.exe
else
	VENV=venv
	PYTHON_VERSION=3
	PYTHON=$(VENV)/bin/python$(PYTHON_VERSION)
	SAFETY=$(VENV)/bin/safety
endif

# test environnement
hello:
	@echo OS                    = $(OS)
	@echo VENV                  = $(VENV)
	@echo Python exec           = $(PYTHON)
	@echo Safety exec           = $(SAFETY)
	@echo Should we upgrade pip? $(UPGRADE_PIP)

## environnement
clean-venv:
ifeq ($(OS),Windows_NT)
	@echo Removing virutal env is only supported in Linux platforms. Please do it manually for more consistency before launching this command
else
	rm -rf $(VENV)
endif

add-venv:
ifeq ($(OS),Windows_NT)
	python -m venv $(VENV)
else
	python$(PYTHON_VERSION) -m venv $(VENV)
endif

install-dev:
ifeq ($(UPGRADE_PIP),yes)
	$(PYTHON) -m pip install --upgrade pip
endif
	$(PYTHON) -m pip install -r requirements-dev.txt

install:
	$(PYTHON) -m pip install -r requirements.txt

init: clean-venv add-venv install-dev install


## linter and mypy
lint:
	$(PYTHON) -m pylint $(dir) --rcfile ./setup.cfg

mypy:
	$(PYTHON) -m mypy $(dir) --ignore-missing-imports --strict --no-warn-return-any --implicit-reexport --config-file ./setup.cfg

black:
	$(PYTHON) -m black $(dir) --check

flake:
	$(PYTHON) -m flake8 $(dir) --config ./setup.cfg

isort:
	$(PYTHON) -m isort $(dir) --check-only --settings-file ./setup.cfg

format:
	$(PYTHON) -m black $(dir)
	$(PYTHON) -m isort $(dir) --settings-file ./setup.cfg

check: black isort flake lint mypy

## unit tests and coverage
test:
	$(PYTHON) -m pytest $(dir) -vv --capture=tee-sys

coverage:
	$(PYTHON) -m pytest $(dir) --cov-config=.coveragerc --cov=$(dir)

coverage-html:
	$(PYTHON) -m pytest $(dir) --cov-config=.coveragerc --cov=$(dir) --cov-report html


clean-logs:
ifeq ($(OS),Windows_NT)
	@echo Cleaning logs are only supported in Linux platforms
else
	rm -r .output
	rm -r .mypy_cache
	rm -r .pytest_cache
	rm -r htmlcov
	find $(dir) -path '*/__pycache__*' -delete
	find $(dir) -path '*/.ipynb_checkpoints*' -delete
endif

## jupyter kernels
jupyter-venv-add:
	$(PYTHON) -m ipykernel install --name=$(dir) --user

jupyter-venv-remove:
	$(PYTHON) -m jupyter kernelspec uninstall $(dir) -y



safety:
	$(SAFETY) check

setup: init jupyter-venv-add
