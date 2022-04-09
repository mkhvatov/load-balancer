DC_FILE := docker-compose.yml

DC_CMD = docker-compose -f ${DC_FILE}

.PHONY: build stop up


help:
	@echo ""
	@echo "Please use \`make <target>' where <target> is one of"
	@echo ""
	@echo "  build              to make all docker assembly images"
	@echo "  stop               to stop all running containers"
	@echo "  up                 to run all containers"
	@echo ""
	@echo "See contents of Makefile for more targets."

build:
	$(DC_CMD) build

stop:
	$(DC_CMD) down

up: stop
	$(DC_CMD) up
