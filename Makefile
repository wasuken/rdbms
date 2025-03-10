PHONY: test

test:
	bash -c "source .venv/bin/activate && python -m pytest ./tests/test_*.py"
