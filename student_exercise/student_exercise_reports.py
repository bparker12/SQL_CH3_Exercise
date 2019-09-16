import sqlite3

class Student:

    def __init__(self, first, last, handle, cohort):
        self.first_name = first
        self.last_name = last
        self.handle = handle
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} is in cohort {self.cohort}'

class Cohort:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Cohort {self.name}'

class Exercises:

    def __init__(self, eid, lang,   name):
        self.exerciseId = eid
        self.lang = lang
        self.name = name

    def __repr__(self):
        return f'This exercise is called {self.name}, and you are to use {self.lang} language'

class Instructor:

    def __init__(self, iid, first, last, handle, special, name):
        self.instructor_id = iid
        self.first_name = first
        self.last_name = last
        self.handle = handle
        self.special_skill = special
        self.cohort_name = name

    def __repr__(self):
        return f'{self.first_name} is in cohort {self.cohort_name}'


class report():

        def __init__(self):
            self.db_path = "/Users/stuff/workspace/python/SQL/Ch3_StudentExercise3/student_exercise/studentexercises.db"

        def all_cohorts(self):

            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = lambda cursor, row: Cohort(row[0])
                db_cursor = conn.cursor()

                db_cursor.execute("""
                select
                    c.Name
                from Cohort c
                """)

                all_cohorts = db_cursor.fetchall()

                for cohort in all_cohorts:
                    print("cohort")
                    print(cohort)

        def all_exercises(self):

            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = lambda cursor, row: Exercises(row[0], row[1], row[2])
                db_cursor = conn.cursor()

                db_cursor.execute("""
                select
                    e.Id,
                    e.dev_language,
                    e.name
                from Exercise e
                """)

                all_exercises = db_cursor.fetchall()

                for exercise in all_exercises:
                    print("exercises")
                    print(exercise)

                for exercise in all_exercises:
                    if exercise.lang == "javascript":
                        print('javascript only')
                        print(exercise)
                    else:
                        pass


        def all_python_exercises(self):

            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = lambda cursor, row: Exercises(row[0], row[1], row[2])
                db_cursor = conn.cursor()

                db_cursor.execute("""
                select
                    e.Id,
                    e.dev_language,
                    e.name
                from Exercise e
                where e.dev_language = "python"
                """)

                all_python_exercises = db_cursor.fetchall()

                for exercise in all_python_exercises:
                    print("exercises python only")
                    print(exercise)


        def all_instructors(self):

            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = lambda cursor, row: Instructor(row[0], row[1], row[2], row[3], row[4], row[5])
                db_cursor = conn.cursor()

                db_cursor.execute("""
                SELECT
                    i.id,
                    i.first_name,
                    i.last_name,
                    i.slack_handle,
                    i.speciality,
                    c.Name
                from Instructor i
                JOIN Cohort c
                ON i.CohortId = c.Id
                ORDER by c.Id
                """)

                all_instructors = db_cursor.fetchall()

            for instructor in all_instructors:
                print(instructor)


cohort = report()
cohort.all_cohorts()
cohort.all_exercises()
cohort.all_python_exercises()
cohort.all_instructors()


                    # s.first_name,
                    # s.last_name,
                    # i.first_name,
                    # i.last_name

                #                     join Student s
                # on s.CohortId = c.Id
                # join Instructor i
                # on i.CohortId = c.Id