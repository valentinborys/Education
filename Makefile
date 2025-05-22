build:
	docker build --rm -t tnxhub-e2e .

test: build
	docker run --rm -v $(shell pwd):/data -v /dev/shm:/dev/shm tnxhub-e2e
