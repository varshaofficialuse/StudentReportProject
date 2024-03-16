from django.contrib import admin
from .models import *
from django.db.models import Sum
# Register your models here.
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(StudentId)
admin.site.register(Subject)

class StudentMarkAdmin(admin.ModelAdmin):#by using this we can show below columns in admin panel
    list_display=['student', 'subject','marks']
   

admin.site.register(SubjectMarks,StudentMarkAdmin)


class StudentRankAdmin(admin.ModelAdmin):#by using this we can show below columns in admin panel
    list_display=['student','total_marks', 'student_rank','date_of_report_generation']
    ordering=['student_rank']

    def total_marks(self,obj):
        subject_marks=SubjectMarks.objects.filter(student=obj.student)
        marks=(subject_marks.aggregate(Sum('marks')))
        return (marks['marks__sum'])
    
admin.site.register(StudentRank,StudentRankAdmin)