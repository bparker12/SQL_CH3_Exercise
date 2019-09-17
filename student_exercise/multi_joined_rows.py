import sqlite3



class Exercise():

    def __init__(self):
            self.db_path = "/Users/stuff/workspace/python/SQL/Ch3_StudentExercise3/student_exercise/studentexercises.db"


    def multi_join(self):

        with sqlite3.connect(self.db_path) as conn:
            exercises = dict()

            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.Id,
                    e.name,
                    s.Id,
                    s.first_name,
                    s.last_name
                from Exercise e
                join Student_Exercises se on se.ExerciseId = e.Id
                join Student s on s.Id = se.StudentId
            """)

            dataset = db_cursor.fetchall()

            # for row in dataset:
            # exercise_id = row[0]
            # exercise_name = row[1]
            # student_id = row[2]
            # student_name = f'{row[3]} {row[4]}'

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
                for student in students:
                    print(f'\t* {student}')

exercise = Exercise()
exercise.multi_join()