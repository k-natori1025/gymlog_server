build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

shell:
	docker-compose exec app bash

app-migrate:
	docker compose exec api bash -c "cd app/database && poetry run alembic upgrade head"

setup:
	@make up
	@make app-migrate
