from django.contrib import admin
from .models import Student


# Register your models here.
admin.site.register(Student)


# password for admin
# admin - parag 
# password - 12345


# here i am adding adition functionality to add students detail using this please uncomment it if you want to add another student detail

# Create a new student
# student = Student.objects.create(name='arti wasnik', total_marks=45)