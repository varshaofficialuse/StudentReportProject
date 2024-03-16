from django.db import models

# Create your models here.

class Department(models.Model):
    department=models.CharField(max_length=100)

    class Meta:
        ordering=['department']

class StudentId(models.Model):
    student_id=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.student_id
    
class Subject(models.Model):
    subject_name=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.subject_name

class Student(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE,related_name="depart")
    student_id=models.ForeignKey(StudentId,on_delete = models.CASCADE,related_name="studentid")
    student_name= models.CharField(max_length=100)
    student_email =models.EmailField(unique=True) 
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()

    def __str__(self) -> str:
        return self.student_name
    class Meta:
        ordering=['student_name']
        verbose_name='student'

class SubjectMarks(models.Model):
    
    student=models.ForeignKey(Student,related_name="studentmarks",on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,related_name="subject",on_delete=models.CASCADE)
    marks = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.student.student_name} {self.subject.subject_name}"

    class Meta:
        unique_together = ['student','subject']#this is used to maintain the uniqueness where one student should not repeat same subject again


class StudentRank(models.Model):
    student=models.ForeignKey(Student,related_name="studentrank",on_delete=models.CASCADE)
    student_rank=models.IntegerField()
    date_of_report_generation=models.DateField(auto_now_add=True)
    
    class Meta:
        unique_together=['student_rank','date_of_report_generation']