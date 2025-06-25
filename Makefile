.DEFAULT_GOAL := help

.PHONY: \
	cleanup \
	debug \
	distclean \
	format \
	freeze \
	help \
	lint \
	setup \
	send_prompts \
	test \
	tree \
	typecheck \
	update \
	update_interpreter_path

PROJECT_NAME := $(notdir $(CURDIR))
REPO_DIR=$(GITHUB_PARENT)/$(GITHUB_VSCODE_REPO)
VSCODE_WORKSPACE_FILE := $(REPO_DIR)/workspaces/$(PROJECT_NAME).code-workspace

cleanup: ## Remove Python caches and build artifacts
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type f -name '*.py[co]' -delete
	rm -rf .pytest_cache .ruff_cache .mypy_cache
	@echo "🧹 Cleanup complete."

debug:
	@echo "REPO_DIR: $(REPO_DIR)"
	@echo "VSCODE_WORKSPACE_FILE: $(VSCODE_WORKSPACE_FILE)"
	@ls -l "$(VSCODE_WORKSPACE_FILE)"

distclean: ## Remove all caches and Hatch environment
	hatch env remove default || true
	make cleanup

format: ## Format code with Ruff
	hatch run format

freeze: ## Freeze requirements
	hatch run pip freeze > requirements.txt

# Auto-generate help from target comments
help: ## Show this help
	@awk 'BEGIN {FS = ":.*?## "}; /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

lint: ## Run Ruff linter
	hatch run lint

setup: ## Create the hatch environment
	mypy --install-types
	hatch env create
	make freeze

send_prompts: ## Send the prompts to Nvidia Deepseek
	hatch run python deepseek_nvidia/send_prompts.py

test: ## Run all tests
	hatch run test

tree: ## list contents of directories in a tree-like format
	tree -I '__pycache__|.git|.hatch' -a -F

typecheck: ## Run mypy type checks
	hatch run type_check

update: ## Update all packages inside the Hatch environment
	hatch run update
	make freeze

update_interpreter_path: ## Update python.defaultInterpreterPath using Hatch environment
	@bash -c '\
		echo "Detecting Hatch environment path..."; \
		env_path="$$(hatch env find)"; \
		if [[ "$$OSTYPE" == "msys" || "$$OSTYPE" == "win32" ]]; then \
			python_path="$${env_path//\//\\\\}\\\\Scripts\\\\python.exe"; \
		else \
			python_path="$$env_path/bin/python"; \
		fi; \
		if [[ ! -f "$(VSCODE_WORKSPACE_FILE)" ]]; then \
			echo "{}" > "$(VSCODE_WORKSPACE_FILE)"; \
		fi; \
		echo "✔ Updating python.defaultInterpreterPath to: $$python_path"; \
		jq --arg path "$$python_path" \
			'"'"'. + {"python.defaultInterpreterPath": $path}'"'"' \
			"$(VSCODE_WORKSPACE_FILE)" | sponge "$(VSCODE_WORKSPACE_FILE)"; \
		echo "✔ Updated $(VSCODE_WORKSPACE_FILE)"; \
		echo "Validating JSON..."; \
		jq empty "$(VSCODE_WORKSPACE_FILE)" && echo "✅ JSON is valid." || \
			{ echo "❌ JSON is invalid."; exit 1; }'








