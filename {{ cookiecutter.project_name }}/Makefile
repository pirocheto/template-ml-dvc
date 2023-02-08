#################################################################################
# GLOBAL COMMANDS                                                               #
#################################################################################

# Delete all compiled Python files
.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

# Install env manager
# For more details see: https://python-poetry.org/docs/#installation
.PHONY: install-poetry
install-poetry:
	curl -sSL https://install.python-poetry.org | python3 -

# Install all dependencies in current env
.PHONY: install-deps
install-deps:
	poetry install --no-root

# Install pre-commit hook
.PHONY: pre-commit
pre-commit:
	pre-commit install

## Upload Data to default DVC remote
push:
	dvc push

## Download Data from default DVC remote
pull:
	dvc pull

#################################################################################
# PROJECT COMMANDS                                                              #
#################################################################################

# Run an experiment
.PHONY: run
run:
	dvc exp run

# Run project to reproduce experiment
.PHONY: repro
repro:
	dvc repro

# Show experiments in a table format
.PHONY: show
show:
	dvc exp show  --drop "data|models|src"

# Open a html file containing plots
.PHONY: plots
plots:
	dvc plots show

