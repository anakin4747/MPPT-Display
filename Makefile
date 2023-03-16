# Define variables
VENV_NAME := env
PYTHON := $(VENV_NAME)/bin/python3
PIP := $(VENV_NAME)/bin/pip3
PROJECT_NAME := VIVPusbPlot.py

# Default target runs project
run:
	@sudo $(PYTHON) $(PROJECT_NAME)

# Set up virtual environment
venv:
	$(PYTHON) -m venv $(VENV_NAME)
	$(PIP) install --upgrade pip

# Install project dependencies
deps: venv
	$(PIP) install -r requirements.txt

# Clean up generated files
clean:
	@rm -f logs/measured*

