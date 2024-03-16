from faker import Faker
import random
from .models import *
from django.db.models import Sum

fake=Faker()
def create_sub_marks(n):
    try:
        student_obj=Student.objects.all()
        for student in student_obj:
            subjects=Subject.objects.all()
            for subject in subjects:
                SubjectMarks.objects.create(
                    subject=subject,
                    student=student,
                    marks=random.randint(30,100)
                )

    except Exception as e:
        print(e)

def fakedata(n=10)->None:
    try:
        for i in range(n):
            department_obj=Department.objects.all()
            random_idx=random.randint(0,len(department_obj)-1)
            student_id=f"STU-0{random.randint(100,999)}"
            department=department_obj[random_idx]
            student_name=fake.name()
            student_email=fake.email()
            student_age =random.randint(20,30)
            student_address = fake.address()

            stuent_id_obj=StudentId.objects.create(student_id=student_id)
            student_obj=Student.objects.create(department=department,
                                               student_id=stuent_id_obj,
                                               student_name=student_name,
                                               student_email=student_email,
                                               student_age=student_age,
                                               student_address=student_address
                                               )

    except Exception as e:
        print(e)

def generate_rank():
    current_rank=-1
    i=1
    ranks=Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks','-student_age')
    for rank in ranks:
        StudentRank.objects.create(
            student=rank,
            student_rank=i
        )
        i+=1