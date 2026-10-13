import os
import re
import sqlite3
from datetime import datetime, timezone

DB_PATH = os.environ.get("STUDENT_DB_PATH", "students.db")

def connect():
    connection = sqlite3.connect(DB_PATH, timeout=10)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection

def init_db():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                course TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """)

def validate_student(name, email, course):
    name = (name or "").strip()
    email = (email or "").strip()
    course = (course or "").strip()
    if not name or not email or not course:
        return False, "All fields are required."
    if len(name) > 100 or len(course) > 100 or len(email) > 150:
        return False, "One or more fields exceed the allowed length."
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        return False, "Enter a valid email address."
    return True, "Valid input."

def add_student(name, email, course):
    valid, message = validate_student(name, email, course)
    if not valid:
        raise ValueError(message)
    created_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with connect() as conn:
        cursor = conn.execute(
            "INSERT INTO students(name, email, course, created_at) VALUES (?, ?, ?, ?)",
            (name.strip(), email.strip(), course.strip(), created_at),
        )
        return cursor.lastrowid

def get_students():
    with connect() as conn:
        return conn.execute(
            "SELECT id, name, email, course, created_at FROM students ORDER BY id DESC"
        ).fetchall()

def delete_student(student_id):
    with connect() as conn:
        cursor = conn.execute("DELETE FROM students WHERE id = ?", (int(student_id),))
        return cursor.rowcount > 0

def get_student_count():
    with connect() as conn:
        return conn.execute("SELECT COUNT(*) FROM students").fetchone()[0]
