from django.db import models

class Principal(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Add other fields as needed


from django.contrib.auth.hashers import make_password

def create_principal():
    Principal.objects.create(
        username='principal_username',
        password=make_password('principal_password'),
        # Set other field values
    )

from django.db import models

class Notification(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    admission_date = models.DateField()
    grade = models.CharField(max_length=10)
    performance = models.TextField()  # Academic performance details
    attendance_records = models.TextField()  # Attendance records (e.g., JSON format)
    disciplinary_actions = models.TextField()  # Disciplinary actions
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_fee = models.DecimalField(max_digits=10, decimal_places=2)
    attendance_percentage = models.FloatField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

from django.db import models

class Teacher(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

