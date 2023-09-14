.PHONY: all
all: codestyle typecheck lint test

.PHONY: codestyle
codestyle:
	black -l 79 src/ tests/

.PHONY: typecheck
typecheck:
	mypy --ignore-missing-imports src/

.PHONY: lint
lint:
	pylint src/

.PHONY: test
test:
	pytest tests/

.PHONY: clean
clean:
	find . -type f -name "*.pyc" | xargs rm -fr
	find . -type d -name __pycache__ | xargs rm -fr
