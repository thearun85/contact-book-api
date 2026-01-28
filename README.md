# Contact Book API v2

Modern Contact Book API built with Flask, SQLAlchemy, and Pydantic.

## Features

- Clean Architecture (Layers: API -> Service -> Repository -> Database)
- Type hints everywhere (mypy compliant)
- Pydantic validation
- Modern Python 3.11+ features
- Docker support

## Tech Stack

- **Flask** - Web framework
- **SQLAlchemy 2.0** - ORM
- **Pydantic** - Data validation
- **PostgreSQL** - Database
- **Poetry** - Dependency management
- **Pytest** - Testing
- **Ruff** - Linting
- **Mypy** - Type checking

## Setup 

### Prerequisites
- Python 3.11+
- Poetry
- Docker & Docker Compose (optional)

### Installation
```bash
# Clone repository
git clone
cd contact-book-api

# Install dependencies
poetry install

# Copy environment file
cp .env.example .env

# Activate virtual environment
poetry shell
```

## Project Structure
```
app/
|__api/				# API endpoints (routes)
|
|__core/			# Core functionality (config, database, logging)
|
|__models/			# SQLAlchemy models
|
|__schemas/			# Pydantic schemas
|
|__services/		# Business logic
|
|__repositories/	# Database operations
```

## Running
```bash
# Development
poetry run flask run

# With Docker
docker compose up
```

## Testing
```bash
# Run tests
poetry run pytest

# With coverage
poetry run pytest --cov=app
```

## Development
```bash
# Type checking
poetry run mypy app/

# Linting
poetry run ruff check app/

# Format
poetry run ruff format app/
```

## Learning Goals

This project demonstrates:
- Clean architecture principles
- Seperation of concerns
- Type safety with mypy
- Modern Python patterns
- Industry-standard tools

