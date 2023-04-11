#!make
#----------------------------------------
# Settings
#----------------------------------------
.DEFAULT_GOAL := help

#--------------------------------------------------
# Targets
#--------------------------------------------------
install: clean ## Creates venv and installs the package
	@echo "==> Creating virtual environment..."
	@python3 -m venv venv/
	@venv/bin/pip install black
	@echo "    [✓]"
	@echo

	@echo "==> Installing utility and dependencies..."
	@venv/bin/pip install --upgrade pip
	@venv/bin/pip install -r requirements.txt
	@echo "    [✓]"
	@echo

uninstall: clean ## Uninstalls utility, deletes data, and destroys venv
	@echo "==> Removing data..."
	@venv/bin/python src/delete.py
	@echo "    [✓]"
	@echo
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

download_pretraining: ## Downloads the raw files used for pretraining the model
	@echo "==> Downloading files..."
	@venv/bin/python src/pretraining/download.py
	@echo "    [✓]"
	@echo

decompress_pretraining: ## Decompresses the raw files used for pretraining the model
	@echo "==> Decompressing files..."
	@venv/bin/python src/pretraining/decompress.py
	@echo "    [✓]"
	@echo

preprocess_pretraining: ## Preprocesses the raw files used for pretraining the model
	@echo "==> Preprocessing files..."
	@venv/bin/python src/pretraining/preprocess.py
	@echo "    [✓]"
	@echo

concat: ## Concat raw files into a single file
	@echo "==> Concatenating files..."
	@venv/bin/python src/concat.py
	@echo "    [✓]"
	@echo

preprocess: ## Preprocess data: Concat files, fix spelling/grammar, remove special characters
	@echo "==> Preprocessing file..."
	@venv/bin/python src/preprocess.py
	@echo "    [✓]"
	@echo


.PHONY: install uninstall clean dwonload concat preprocess clean-special-characters help
help: ## Shows available targets
	@fgrep -h "## " $(MAKEFILE_LIST) | fgrep -v fgrep | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-13s\033[0m %s\n", $$1, $$2}'
