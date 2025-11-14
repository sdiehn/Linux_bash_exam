.PHONY: tests
bash:
	python3 -m venv .linux_venv && \
	source .linux_venv/bin/activate && \
	pip install -r requirements.txt && \
	crontab cron.txt

tests:
	pytest tests/test_collect.py && \
	pytest tests/test_preprocessed.py && \
	pytest tests/test_model.py

all:

