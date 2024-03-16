from . import views
from django.urls import path


urlpatterns = [
    path("getStudents/",views.allStudents,name="getStudents"),
    path("seeMarks/<student_id>",views.seeMarks,name="seeMarks"),
]
