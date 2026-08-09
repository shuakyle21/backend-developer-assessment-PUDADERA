# TODO — Client Project Tracker API

Generated from `docs/REQUIREMENTS.md`, `docs/ARCHITECTURE.md`, `docs/USE_CASES.md`, `docs/SUBMISSION.md`.

## 1. Project scaffolding
- [x] Set up `app/` package per `docs/ARCHITECTURE.md` layout:
  - [x] `app/main.py` — FastAPI app, route registration
  - [x] `app/controllers/projects.py`
  - [x] `app/services/project_service.py`
  - [x] `app/repositories/project_repository.py`
  - [x] `app/models/project.py`
  - [x] `app/schemas/project.py`
- [x] Choose datastore (SQLite) and add dependencies
- [x] Add `requirements.txt` / dependency management
- [x] Wire DB connection/session (`app/database.py`)
- [x] Seed script for sample data (`scripts/seed.py` + `test_data.json` → `data.db`)

## 2. Project model (UC-model)
- [x] Fields: ID, Client Name, Project Name, Description, Status, Priority, Start Date, Due Date
- [x] Define allowed `Status` values (`Planning`, `In Progress`, `On Hold`, `Completed` — checked as a set in the service layer, not a formal `enum.Enum` yet)
- [x] Define allowed `Priority` values (`Low`, `Medium`, `High` — same as above)

## 3. Endpoints (UC1–UC5)
- [x] `GET /projects` — list all projects
- [x] `GET /projects/:id` — retrieve single project (404 if missing)
- [x] `POST /projects` — create project
- [x] `PUT /projects/:id` — update project
- [x] `DELETE /projects/:id` — delete project

## 4. Validation (UC6, `<<include>>` in Create/Update)
- [x] Client Name required
- [x] Project Name required
- [x] Status must be a valid enum value
- [x] Priority must be a valid enum value
- [x] Due Date cannot be earlier than Start Date
- [x] Return meaningful error messages (4xx) for invalid requests (raises on first failing rule via `HTTPException`)
- [x] Validation lives in service layer, not controller/repository

## 5. Error handling
- [x] Consistent error response shape (`{"detail": "..."}` via FastAPI's built-in `HTTPException`)
- [x] 404 for missing project (get/update/delete)
- [x] 422 for validation failures
- [ ] Unhandled exception → 500 with safe message (not explicitly tested)

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
