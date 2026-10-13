import os
import tempfile
import unittest

# Use a temporary database before importing database.py.
_tmp = tempfile.TemporaryDirectory()
os.environ["STUDENT_DB_PATH"] = os.path.join(_tmp.name, "test_students.db")

import database

class StudentDatabaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        database.init_db()

    def setUp(self):
        with database.connect() as conn:
            conn.execute("DELETE FROM students")

    def test_add_and_read_student(self):
        student_id = database.add_student("Asha Kumar", "asha@example.com", "Computer Science")
        rows = database.get_students()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], student_id)
        self.assertEqual(rows[0][1], "Asha Kumar")

    def test_delete_student(self):
        student_id = database.add_student("Ravi", "ravi@example.com", "IT")
        self.assertTrue(database.delete_student(student_id))
        self.assertEqual(database.get_student_count(), 0)

    def test_invalid_email_rejected(self):
        valid, _ = database.validate_student("Test", "not-an-email", "IT")
        self.assertFalse(valid)

    def test_required_fields(self):
        valid, _ = database.validate_student("", "a@example.com", "IT")
        self.assertFalse(valid)

if __name__ == "__main__":
    unittest.main()
