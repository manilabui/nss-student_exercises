import sqlite3
from student import Student
from cohort import Cohort
from exercise import Exercise

class Report():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = '/Users/manilabui/workspace/nss/backend/python/student_exercises/exercises.db'

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(row[1], row[2], row[3], row[5])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT 
                s.id,
                s.firstName,
                s.lastName,
                s.slack,
                s.cohortId,
                c.name
            FROM Student s
            JOIN Cohort c on s.cohortId = c.Id
            ORDER BY s.cohortId
            """)

            all_students = db_cursor.fetchall()

            [print(s) for s in all_students]

    def all_cohorts(self):

        """Retrieve all cohorts with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(row[0])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT c.name
            FROM Cohort c
            """)

            all_cohorts = db_cursor.fetchall()

            [print(c) for c in all_cohorts]

    def all_exercises(self):

        """Retrieve all exercises with the exercise name + language"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[0], row[1])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                e.name,
                l.languageId
            FROM Exercise e
            JOIN ProgrammingLanguage l ON e.languageId = l.Id
            """)

            all_exercises = db_cursor.fetchall()

            [print(e) for e in all_exercises]

    def exercises_in_x_language(self, language):

        """Retrieve all exercises with the exercise name + language"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[0], row[1])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                e.name,
                l.languageId
            FROM Exercise e
            JOIN ProgrammingLanguage l ON e.languageId = l.Id
            WHERE l.name = {language}
            """)

            all_exercises = db_cursor.fetchall()

            [print(e) for e in all_exercises]

    def exercises_with_students(self):

        """Retrieve all exercises + the students working on each one"""

        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                e.Id ExerciseId,
                e.Name,
                s.Id StudentId,
                s.FirstName,
                s.LastName
            FROM Exercise e
            JOIN StudentToExercise se ON se.ExerciseId = e.Id
            JOIN Student s ON s.Id = se.StudentId
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'

                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)

            for exercise_name, students in exercises.items():
                print(exercise_name)
                [print(f'\t* {student}') for student in students]


reports = Report()

reports.all_students()
reports.all_cohorts()
reports.all_exercises()
reports.exercises_with_students()
