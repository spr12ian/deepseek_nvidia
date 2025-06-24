.DEFAULT_GOAL := help

.PHONY: \
	format \
	freeze \
	help \
	lint \
	setup \
	test \
	typecheck \
	update

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
	hatch env create

test: ## Run all tests
	hatch run test

typecheck: ## Run mypy type checks
	hatch run type_check

update: ## Update all packages inside the Hatch environment
	hatch run update
