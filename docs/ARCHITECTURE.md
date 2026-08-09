# Architecture

## Layering

Following REQUIREMENTS.md's recommendation, the API is split into three layers:

- **Controllers** (FastAPI route handlers) — parse HTTP requests, call the service layer, shape HTTP responses/status codes. No business rules here.
- **Services** — business logic and validation rules that must hold true regardless of caller (HTTP, CLI, tests, etc.). Examples: "due date cannot be earlier than start date", "status must be a valid value".
- **Repositories** — data access only (CRUD against the chosen datastore). No validation, no HTTP concerns.

```text
Client (HTTP request)
        │
        ▼
┌───────────────┐
│  Controller    │  parses request, returns HTTP response
└───────┬───────┘
        │ calls
        ▼
┌───────────────┐
│   Service      │  validation + business rules
└───────┬───────┘
        │ calls
        ▼
┌───────────────┐
│  Repository    │  data access (CRUD)
└───────┬───────┘
        │
        ▼
   Datastore
```

## Why this split

Validation rules (required fields, valid status/priority, due date >= start date) live in the **service** layer because they are facts about a Project, independent of how the request arrived. Putting them in the controller would mean duplicating the same checks for `POST /projects` and `PUT /projects/:id`. Putting them in the repository would couple business rules to storage details.

## Suggested module layout

```text
app/
├── main.py                # FastAPI app, route registration
├── controllers/
│   └── projects.py        # route handlers for /projects
├── services/
│   └── project_service.py # validation + business logic
├── repositories/
│   └── project_repository.py  # data access
├── models/
│   └── project.py         # Project schema (Pydantic/ORM model)
└── schemas/
    └── project.py         # request/response DTOs
```
