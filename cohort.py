class Cohort:
    def __init__(self, name):
        self.name = name
        self.instructors = list()
        self.students = list()

    def add_students(self, students):
        self.students.extend(students)

    def add_instructors(self, instructors):
        self.instructors.extend(instructors)
