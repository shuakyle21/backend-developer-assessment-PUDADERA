# Requirements

## Scenario

You are building the backend API for a Client Project Tracker used by a digital agency.

Your API will power project creation, updates, and retrieval for a frontend application.

No frontend is required.

---

## Project Model

Each project contains:

- ID
- Client Name
- Project Name
- Description
- Status
- Priority
- Start Date
- Due Date

---

## API Endpoints

### Get all projects
GET /projects

### Get single project
GET /projects/:id

### Create project
POST /projects

### Update project
PUT /projects/:id

### Delete project
DELETE /projects/:id

---

## Validation Rules

- Client Name is required
- Project Name is required
- Status must be valid
- Priority must be valid
- Due Date cannot be earlier than Start Date

Return meaningful error messages for invalid requests.

---

## Data Storage

You may use any database:

- PostgreSQL
- MySQL
- MongoDB
- SQLite

---

## Technical Requirements

- RESTful API design
- Proper error handling
- Input validation
- Clean architecture (controllers/services/repositories recommended)

---

## Bonus (Optional)

- Pagination
- Search endpoint
- Filtering by status or priority
- Authentication
- Unit tests
- Docker setup
- API documentation (Swagger/Postman)
