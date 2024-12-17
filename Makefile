setup:
	echo "Building Docker image..."
	docker build -t fastapi-app .
	echo "Starting the application with docker-compose..."
	docker-compose up --build

up:
	docker compose -f docker-compose.yml up -d

down:
	docker compose -f docker-compose.yml down && docker network prune --force
