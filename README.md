# Python CI/CD Demo

[![CI Pipeline](https://github.com/SyntaxErrorGo/python-ci-cd-demo/actions/workflows/ci.yml/badge.svg)](https://github.com/SyntaxErrorGo/python-ci-cd-demo/actions/workflows/ci.yml)

Небольшое FastAPI-приложение с автоматизированной проверкой изменений через GitHub Actions.

При каждом push и pull request pipeline запускает тесты, собирает Docker-образ, поднимает приложение через Docker Compose и проверяет его доступность.

## Стек

- Python 3.12
- FastAPI
- pytest
- Docker
- Docker Compose
- GitHub Actions

## Как работает pipeline

```text
push / pull request
        ↓
install dependencies
        ↓
pytest
        ↓
docker build
        ↓
docker compose up
        ↓
healthcheck + API check
        ↓
docker compose down
```

Конфигурация pipeline находится в `.github/workflows/ci.yml`.

## Запуск через Docker Compose

```bash
git clone https://github.com/SyntaxErrorGo/python-ci-cd-demo.git
cd python-ci-cd-demo
docker compose up --build
```

После запуска доступны:

- API: `http://localhost:8000`
- Swagger UI: `http://localhost:8000/docs`
- Healthcheck: `http://localhost:8000/health`

Остановка приложения:

```bash
docker compose down
```

## Локальный запуск тестов

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -v
```

Для Windows активация виртуального окружения выполняется командой:

```powershell
.venv\Scripts\activate
```

## Структура проекта

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```
