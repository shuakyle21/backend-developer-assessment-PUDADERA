import json
import os
import sqlite3

DATABASE_PATH = os.getenv("DATABASE_PATH", "./data.db")

with open("test_data.json") as f:
    projects = json.load(f)

os.makedirs(os.path.dirname(DATABASE_PATH) or ".", exist_ok=True)
conn = sqlite3.connect(DATABASE_PATH)
cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY,
        client_name TEXT NOT NULL,
        project_name TEXT NOT NULL,
        description TEXT,
        status TEXT NOT NULL,
        priority TEXT NOT NULL,
        start_date TEXT NOT NULL,
        due_date TEXT NOT NULL
    )
    """
)

for p in projects:
    cur.execute(
        """INSERT OR REPLACE INTO projects (id, client_name, project_name, description, status, priority, start_date, due_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (p["id"], p["clientName"], p["projectName"], p["description"], p["status"], p["priority"], p["startDate"], p["dueDate"]),
    )

conn.commit()
conn.close()
