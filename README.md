this project is performing all these 2 requirments -

1) Load Student Details API
2) Server-side Filtering API

Evaluation parameters performed -
1. Api functionality completeness
2. Coding standards , readability, originality
3. DB is used
4. Developed UI





Steps to run this project 
-----------------------------------------------------------------------------------------------------------------------------------
To run this project you need to first run this command to install all project relaed dependencies--


'pip install -r requirements.txt'
This command will install all the Python packages listed in the requirements.txt file.

'python manage.py migrate'
This command will apply any pending database migrations

'python manage.py createsuperuser'
Follow the prompts to create a superuser account

'python manage.py runserver'
to run the project use this command
-----------------------------------------------------------------------------------------------------------------------------------


After running the project go to this link in your chrome browser

http://127.0.0.1:8000/students/student_list/  


this link will give the data of students
-----------------------------------------------------------------------------------------------------------------------------------


Additional information - 

To add student details in database here is the steps-

go to the admin.py file they is an option like this fill details and comment out and runserver it will store this info into the database
# student = Student.objects.create(name='arti wasnik', total_marks=45)
-----------------------------------------------------------------------------------------------------------------------------------


credentials of admin -

# password for admin
# admin - parag 
# password - 12345
-----------------------------------------------------------------------------------------------------------------------------------
