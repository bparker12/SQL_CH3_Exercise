import sqlite3

class Student():

    def __init__(self, first, last, handle, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self. cohort}'

class StudentExerciseReport:

        # """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/stuff/workspace/python/SQL/Ch3_StudentExercise3/student_exercise/studentexercises.db"

    # def create_student(self, cursor, row):
    #     return Student(row[1], row[2], row[3], row[5])

    def all_students(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(row[1], row[2], row[3], row[5])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.first_name,
                s.last_name,
                s.slack_handle,
                s.CohortId,
                c.Name
            from Student s
            join Cohort c on s.CohortId = c.Id
            order by s.CohortId
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                # print(f'{student.first_name} {student.last_name} is in {student.cohort}')
                # or
                print(student)
                # or
                # [print(s) for s in all_students]


reports = StudentExerciseReport()
reports.all_students()

