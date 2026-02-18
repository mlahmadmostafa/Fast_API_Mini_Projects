# Lessons Learned

## API Design

- Start simple, then harden:
  - Project 1 proves route mechanics quickly.
  - Project 2 adds validation and clearer error behavior.
  - Project 3 adds persistence, auth, and module boundaries.
- Route specificity matters. Static routes should usually be declared before dynamic ones when they overlap.

## Validation and Contracts

- Pydantic models reduce manual checks and keep request contracts explicit.
- Validation constraints (`min_length`, bounds) move failures to the API edge.
- Keep types consistent across route parameters and model fields to avoid runtime bugs.

## Authentication and Security

- Hash passwords before storage (`passlib` with argon2 here).
- Keep JWT payload minimal (`sub`, `id`, `role`, `exp` is a practical baseline).
- Use dependencies to centralize auth checks, then reuse across routers.
- Secrets should move to environment variables for production use.

## Database and ORM

- Separate DB engine/session setup from models and routes (`database.py` pattern).
- Use one session per request via dependency injection.
- Keep model definitions clean and explicit; enforce ownership at query level (`owner_id` filters in todos).

## Architecture

- Router-per-domain (`auth`, `todos`, `users`, `admin`) scales better than one large file.
- Shared dependencies (`get_db`, `get_current_user`) reduce duplication when standardized.
- Templates and API endpoints can coexist in one app when mounted and routed clearly.

## Testing

- Dependency overrides are the key pattern for FastAPI test isolation.
- A temporary SQLite DB + fixture cleanup is sufficient for early-stage endpoint tests.
- Test both success and failure paths (auth failure, not found, validation errors).

## Migrations

- Alembic gives versioned schema changes and rollback options.
- Keep model metadata wired in `alembic/env.py`.
- Use migration scripts to evolve schema safely instead of editing DB manually.

## Practical Next Improvements

- Add `.env`-based config for secrets and DB URL.
- Add response models for all endpoints.
- Add more tests per router and edge cases.
- Add linting/formatting (`ruff`, `black`) and CI.
- Normalize inconsistent route naming and HTTP method choices.

