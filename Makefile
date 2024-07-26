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

# マイグレーションファイル作成
new-migration:
	@read -p "Enter migration file name: " name; \
	docker compose exec api bash -c "cd app/database && poetry run alembic revision -m \"$$name\""

app-seeder:
	docker compose exec api bash -c "cd app/database && poetry run python master_seeder.py"

setup:
	@make up
	@echo "Waiting for containers to start..."
	@sleep 30
	@make app-migrate
	@make app-seeder
