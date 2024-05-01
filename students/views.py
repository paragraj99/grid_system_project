from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Student

# Create your views here.

def student_list(request):
    name_contains = request.GET.get('name_contains')
    total_marks_gt = request.GET.get('total_marks_gt')
    
    students = Student.objects.all()
    
    if name_contains:
        students = students.filter(name__icontains=name_contains)
    if total_marks_gt:
        students = students.filter(total_marks__gt=total_marks_gt)

    data = {
        'students': students,
    }
    return render(request, "student_list.html", {'data': data})