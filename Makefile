# Makefile

DOCKER_COMPOSE = docker compose

up:
	@$(DOCKER_COMPOSE) up

down:
	@$(DOCKER_COMPOSE) down

restart:
	@$(DOCKER_COMPOSE) down
	@$(DOCKER_COMPOSE) up --build
