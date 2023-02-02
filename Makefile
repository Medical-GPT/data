#!make
#----------------------------------------
# Settings
#----------------------------------------
.DEFAULT_GOAL := help
#--------------------------------------------------
# Variables
#--------------------------------------------------

#--------------------------------------------------
# Targets
#--------------------------------------------------
install: clean ## Creates venv and installs the package
	@echo "==> Creating virtual environment..."
	@python3 -m venv venv/
	@venv/bin/pip install black
	@venv/bin/pip install isort
	@echo "    [✓]"
	@echo

	@echo "==> Installing utility and dependencies..."
	@venv/bin/pip install --upgrade pip
	@venv/bin/pip install -r requirements.txt
	@echo "    [✓]"
	@echo

uninstall: clean ## Uninstalls utility and destroys venv
	@echo "==> Uninstalling utility and dependencies..."
	@rm -rf venv/
	@echo "    [✓]"
	@echo

clean: ## Cleans up temporary files
	@echo "==> Cleaning up..."
	@find . -name "*.pyc" -exec rm -f {} \;
	@echo "    [✓]"
	@echo

download: ## Downloads the raw files used for training
	@echo "==> Downloading files..."
	@venv/bin/python src/download.py
	@echo "    [✓]"
	@echo

concat: ## Concat raw files into a single file
	@echo "==> Concatenating files..."
	@venv/bin/python src/concat.py
	@echo "    [✓]"
	@echo

preprocess: ## Preprocess concatenated file (created if not present)
	@echo "==> Preprocessing file..."
	@venv/bin/python src/preprocess.py
	@echo "    [✓]"
	@echo

	

.PHONY: install uninstall clean help
help: ## Shows available targets
	@fgrep -h "## " $(MAKEFILE_LIST) | fgrep -v fgrep | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-13s\033[0m %s\n", $$1, $$2}'
