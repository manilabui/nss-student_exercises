class Instructor:
		def __init__(self, first_name, last_name):
				self.first_name = first_name
				self.last_name = last_name

		def __str__(self):
				return f'{self.first_name} {self.last_name}'

		def add_slack(self, handle):
				self.slack = handle

		def set_cohort(self, cohort):
				self.cohort = cohort

		def set_specialty(self, specialty):
				self.specialty = specialty

		def assign_exercises(self, students, exercises):
				return [ student.add_exercises(exercises) for student in students ]