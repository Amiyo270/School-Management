from school import School
from persons import Student, Teacher
from subjects import Subject
from ClassRoom import ClassRoom

school = School("ABC", "Sylhet")


eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

Aitijya = Student("Aitijya", eight)
Jagoron = Student("Jagoron", nine)
Amiyo = Student("Amiyo", ten)
Diya = Student("Diya", ten)

school.student_admission(Aitijya)
school.student_admission(Jagoron)
school.student_admission(Amiyo)
school.student_admission(Diya)

akash = Teacher("Akash Das")
prokash = Teacher("Prokash Das")
priyo = Teacher("Priyo Paul")

bangla = Subject("Bangla", akash)
physics = Subject("Physics", prokash)
chemistry = Subject("Chemistry", priyo)
biology = Subject("Biology", priyo)

eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)
nine.add_subject(biology)
nine.add_subject(physics)
nine.add_subject(chemistry)
ten.add_subject(chemistry)
ten.add_subject(physics)
ten.add_subject(bangla)
ten.add_subject(biology)

eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)