from django.shortcuts import render
from .models import Student,ClassRoom
# Create your views here.

def index(request):
    return render(request, 'student/index.html')

def students(request):
    students_list = Student.objects.all()
    return render(request, 'student/students.html', context={'students': students_list})
