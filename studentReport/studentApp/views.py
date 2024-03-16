from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
from django.db.models import Q,Sum
from .fakedata import *

def allStudents(request):
    queryset=Student.objects.all()
    
    if request.GET.get('search'):
        search=request.GET.get('search')
        queryset=queryset.filter(Q(student_name__icontains=search)|
                                 Q(student_id__student_id__icontains=search)|
                                 Q(department__department__icontains=search)|
                                 Q(student_address__icontains=search)|
                                 Q(student_age__icontains=search)|
                                 Q(student_email__icontains=search)
                                 )
    paginator = Paginator(queryset, 10)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'studentApp/getStudents.html',{"queryset":page_obj})

def seeMarks(request,student_id):
    # generate_rank()
    queryset=SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    total_marks=queryset.aggregate(total_marks=Sum('marks'))
   
    return render(request,"studentApp/seeMarks.html",{"queryset":queryset,"total_marks":total_marks})