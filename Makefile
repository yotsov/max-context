.DEFAULT_GOAL := help
.PHONY: help

help: # Displays help for each of the Makefile recipes
	@grep -E '^[a-zA-Z0-9 -]+:.*#' Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

create-env: # Creates a conda environment
	conda env create -f environment.yaml

update-env: # Updates the conda environment
	conda env update -f environment.yaml

code-checks: # Perform all dev checks
	pytest ./max_context/
	mypy ./max_context/ --strict
	ruff format ./max_context/
	ruff check ./max_context/ --fix
	vulture ./max_context/

run: # Run the program, for example with: make model=mistral:7b-instruct-v0.3-q4_K_M run
	ollama pull $(model)
	python -c 'import max_context.run; max_context.run.main("$(model)")'

clean: # Delete temp python folders
	rm -rf ./max_context/__pycache__/
	rm -rf ./.mypy_cache/
	rm -rf ./.pytest_cache/
	rm -rf ./.ruff_cache/