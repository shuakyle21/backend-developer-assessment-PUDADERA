# Use Case Diagram

Generated from `docs/REQUIREMENTS.md`.

```mermaid
%%{init: {'theme': 'dark'}}%%
flowchart LR
    User((API Client))

    subgraph ClientProjectTracker [Client Project Tracker API]
        UC1(["View All Projects"])
        UC2(["View Project Details"])
        UC3(["Create Project"])
        UC4(["Update Project"])
        UC5(["Delete Project"])
        UC6(["Validate Project Data"])
        UC7(["Search / Filter Projects"])
        UC8(["Paginate Results"])
    end

    User --- UC1
    User --- UC2
    User --- UC3
    User --- UC4
    User --- UC5
    User --- UC7

    UC3 -.->|"<<include>>"| UC6
    UC4 -.->|"<<include>>"| UC6
    UC1 -.->|"<<extend>>"| UC7
    UC1 -.->|"<<extend>>"| UC8

    classDef actor fill:#4a148c,stroke:#ba68c8,color:#fff
    classDef usecase fill:#bf360c,stroke:#ff8a65,color:#fff

    class User actor
    class UC1,UC2,UC3,UC4,UC5,UC6,UC7,UC8 usecase
```

## Actors

| Actor      | Description                                                                                                                                                        |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| API Client | Any consumer of the REST API (frontend app, script, or third-party tool) performing project CRUD operations. Requirements define a single actor; no roles specified. |

## Use Cases

| ID  | Use Case                 | Description                                                                                                                              | Actor(s)   |
| :-- | :------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------- | :--------- |
| UC1 | View All Projects         | `GET /projects` — retrieve the list of all projects                                                                                        | API Client |
| UC2 | View Project Details      | `GET /projects/:id` — retrieve a single project by ID                                                                                       | API Client |
| UC3 | Create Project             | `POST /projects` — create a new project record                                                                                             | API Client |
| UC4 | Update Project             | `PUT /projects/:id` — update an existing project                                                                                            | API Client |
| UC5 | Delete Project             | `DELETE /projects/:id` — remove a project                                                                                                   | API Client |
| UC6 | Validate Project Data      | Enforce required fields (Client Name, Project Name), valid Status/Priority, and Due Date ≥ Start Date; returns meaningful error messages   | —          |
| UC7 | Search / Filter Projects   | Bonus: search projects and filter by status or priority                                                                                     | API Client |
| UC8 | Paginate Results           | Bonus: paginate the project list response                                                                                                   | —          |

Notes:

- UC6 is modeled as `<<include>>` in Create and Update since validation is mandatory per `docs/REQUIREMENTS.md`.
- UC7/UC8 are modeled as `<<extend>>` on View All Projects since Pagination, Search, and Filtering are listed under "Bonus (Optional)", not core endpoints.
- Authentication and Unit Tests are also bonus items but aren't modeled as use cases — no distinct actor/role is defined in the requirements.
