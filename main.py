from student import Student
from instructor import Instructor
from cohort import Cohort
from exercise import Exercise

cohort_1 = Cohort('Day 36')
cohort_2 = Cohort('Evening 12')
cohort_3 = Cohort('Evening 13')

exercise_1 = Exercise('Chicken Monkey', 'Javascript')
exercise_2 = Exercise('Daily Journal', 'Javascript')
exercise_3 = Exercise('Pizza', 'Python')
exercise_4 = Exercise('Student Exercises', 'Python')

student_1 = Student('Manila', 'Bui')
student_2 = Student('Matt', 'Blagg')
student_3 = Student('Ryan', 'Cunningham')
student_4 = Student('Corri', 'Golden')

instructor_1 = Instructor('Joe', 'Shepherd')
instructor_2 = Instructor('Jisie', 'David')
instructor_3 = Instructor('Jenna', 'Solis')

students = [student_1, student_2, student_3, student_4]
instructors = [instructor_1, instructor_2, instructor_3]

for student in students:
    student.set_cohort(cohort_1)

for instructor in instructors:
    instructor.set_cohort(cohort_1)

instructor_1.assign_exercises(students, [exercise_3, exercise_4])
instructor_2.assign_exercises(students, [exercise_1, exercise_2])

for student in students:
    print(student)
