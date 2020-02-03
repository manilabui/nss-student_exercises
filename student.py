class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.exercises = list()

    def __str__(self):
        exercise_names = ('\n * ').join([ exercise.name for exercise in self.exercises ])
        return f'{self.first_name} {self.last_name} is working on: \n * {exercise_names}'

    def add_slack(self, handle):
        self.slack = handle

    def set_cohort(self, cohort):
        self.cohort = cohort

    def add_exercises(self, exercises):
        self.exercises.extend(exercises)
