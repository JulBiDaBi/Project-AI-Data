# Build the docker image
build:
	docker build -t fraud-detection .

# Run the data preparation (Phase 1)
data:
	docker run --rm -v $(PWD)/data:/app/data fraud-detection python src/pipeline.py

# Run unit tests
test:
	docker run --rm fraud-detection pytest tests/