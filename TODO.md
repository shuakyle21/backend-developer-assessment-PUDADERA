# TODO — Client Project Tracker API

Generated from `docs/REQUIREMENTS.md`, `docs/ARCHITECTURE.md`, `docs/USE_CASES.md`, `docs/SUBMISSION.md`.

## 1. Project scaffolding
- [ ] Set up `app/` package per `docs/ARCHITECTURE.md` layout:
  - [ ] `app/main.py` — FastAPI app, route registration
  - [ ] `app/controllers/projects.py`
  - [ ] `app/services/project_service.py`
  - [ ] `app/repositories/project_repository.py`
  - [ ] `app/models/project.py`
  - [ ] `app/schemas/project.py`
- [ ] Choose datastore (PostgreSQL/MySQL/MongoDB/SQLite) and add dependencies
- [ ] Add `requirements.txt` / dependency management
- [ ] Wire DB connection/session (e.g. SQLAlchemy engine or Motor client)

## 2. Project model (UC-model)
- [ ] Fields: ID, Client Name, Project Name, Description, Status, Priority, Start Date, Due Date
- [ ] Define allowed `Status` values (enum)
- [ ] Define allowed `Priority` values (enum)

## 3. Endpoints (UC1–UC5)
- [ ] `GET /projects` — list all projects
- [ ] `GET /projects/:id` — retrieve single project (404 if missing)
- [ ] `POST /projects` — create project
- [ ] `PUT /projects/:id` — update project
- [ ] `DELETE /projects/:id` — delete project

## 4. Validation (UC6, `<<include>>` in Create/Update)
- [ ] Client Name required
- [ ] Project Name required
- [ ] Status must be a valid enum value
- [ ] Priority must be a valid enum value
- [ ] Due Date cannot be earlier than Start Date
- [ ] Return meaningful, structured error messages (4xx) for invalid requests
- [ ] Validation lives in service layer, not controller/repository

## 5. Error handling
- [ ] Consistent error response shape
- [ ] 404 for missing project (get/update/delete)
- [ ] 422/400 for validation failures
- [ ] Unhandled exception → 500 with safe message

## 6. Bonus (optional, per rubric weight vs. effort)
- [ ] UC8: Pagination on `GET /projects`
- [ ] UC7: Search endpoint / query param
- [ ] UC7: Filtering by status and/or priority
- [ ] Authentication
- [ ] Unit tests (services + repositories + endpoint tests)
- [ ] Docker setup (Dockerfile + docker-compose)
- [ ] API documentation (FastAPI auto Swagger is free; verify `/docs` works, consider Postman collection)

## 7. Documentation (SUBMISSION.md)
- [ ] README: setup instructions
- [ ] README: technology choices
- [ ] README: how to run the application
- [ ] README: assumptions made
- [ ] Technical Reflection section answering:
  - [ ] Why this implementation approach?
  - [ ] What tradeoffs were made?
  - [ ] What would be improved with more time?
  - [ ] Most challenging part?
  - [ ] AI tools used — which, and how?

## 8. Final checks before submission
- [ ] All endpoints manually tested (curl/Postman/Swagger UI)
- [ ] Validation errors verified for each rule
- [ ] Repo pushed to GitHub, link ready
- [ ] `main.py` placeholder at repo root removed/replaced or reconciled with `app/main.py`
