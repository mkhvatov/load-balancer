SERVICE = balancer
TEST_SERVICE = balancer_test

DC_FILE := docker-compose.yml

DC_CMD = docker-compose -f ${DC_FILE}
TEST_CMD := $(DC_CMD) run --rm $(TEST_SERVICE) python -m pytest

.PHONY: build stop up test


help:
	@echo ""
	@echo "Please use \`make <target>' where <target> is one of"
	@echo ""
	@echo "  build              to make all docker assembly images"
	@echo "  stop               to stop all running containers"
	@echo "  up                 to run all containers"
	@echo "  test               to run tests"
	@echo ""
	@echo "See contents of Makefile for more targets."

build:
	$(DC_CMD) build

stop:
	$(DC_CMD) down

up: stop
	$(DC_CMD) up

test: stop
	$(TEST_CMD)
