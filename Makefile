.PHONY: create-venv clean-venv test-with-venv-local test-with-venv first-release release

# Init new virtual environment
create-venv:
	virtualenv venv --python=python3

# Remove existing virtual environment
clean-venv:
	rm -rf venv

# Test with environment variables saved in .env.local or .env (if .env.local does not exist)
test-with-venv:
	( \
    . venv/bin/activate; \
    pip install -r requirements.txt; \
    . load-environment-variables.sh; \
    python -c "import handler; handler.send_message('', '')"; \
  )

# Run pylint checking
test-with-venv:
	( \
    . venv/bin/activate; \
    pip install -r requirements.txt; \
    pylint handler.py \
  )

# Deploy to AWS lambda
deploy:
	( \
		. load-environment-variables.sh; \
		serverless deploy --aws-profile serverless; \
	)

# Create the first release
first-release:
	npx standard-version --first-release

# Create a new release
release:
	npx standard-version
