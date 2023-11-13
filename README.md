# fsa-rabac

## Description

FastAPI+SQLModel+Alembic+JWT rabac authentication and authorization

## Setup0

1. Set session enviroment variable (options: `dev`, `local`, `prod`):

```bash
    echo "export APP_ENV=dev" >> ~/.bashrc
```

2. Create virtual environment:

```bash
    python3 -m venv .venv
```

3. Activate virtual environment:

```bash
    source .venv/bin/activate
```

4. Install dependencies:

```bash
    pdm install
```