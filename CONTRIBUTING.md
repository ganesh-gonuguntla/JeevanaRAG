# Contributing to JeevanaRAG

Thank you for your interest in improving JeevanaRAG! This document outlines how to get started.

## Development Setup

1. Clone the repository and install dependencies:
   ```bash
   git clone https://github.com/ganesh-gonuguntla/JeevanaRAG.git
   cd JeevanaRAG
   cp .env.example .env
   pip install -r requirements.txt
   ```

2. Start the local stack:
   ```bash
   docker compose up --build -d
   ```

3. Run the test suite:
   ```bash
   python -m pytest tests/ -v
   ```

## Project Structure

| Directory | Purpose |
|---|---|
| `app/` | FastAPI backend â€” graph logic, services, data files |
| `mobile/` | Expo / React Native mobile application |
| `frontend/` | Next.js web frontend |
| `tests/` | Regression and evaluation test suites |
| `scripts/` | Build, evaluation, and maintenance scripts |
| `docs/` | Technical documentation and evaluation plans |

## Code Style

- Python: follow PEP 8 with type annotations
- TypeScript: Prettier + ESLint defaults
- Commit messages: use conventional commit prefixes (`feat:`, `fix:`, `docs:`, `refactor:`, `build:`, `test:`, `chore:`)

## Reporting Issues

Open an issue on GitHub with:
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Python version, Docker version)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
