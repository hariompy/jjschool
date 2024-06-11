from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Notification  # Import the Notification model
from django.shortcuts import render, redirect
from .models import Principal
from django.contrib.auth.hashers import check_password

def principal_login(request):
    hardcoded_username = 'hyy'
    hardcoded_password = 'hyy'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == hardcoded_username and password == hardcoded_password:
            # Hardcoded credentials match, simulate authentication
            principal = Principal.objects.get_or_create(username=username, defaults={'name': 'Your Name', 'email': 'your_email@example.com'})[0]
            request.session['principal_id'] = principal.id
            return redirect('principal_dashboard')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'principal/login.html', {'error_message': error_message})
    else:
        return render(request, 'principal/login.html')


from django.shortcuts import render, redirect
from .models import Notification, Principal
from django.contrib.auth.hashers import check_password
# views.py
def home_page(request):
    notifications = Notification.objects.all().order_by('-created_at')
    information = "Welcome to Our School's Website! Here you'll find all the latest updates and announcements."
    return render(request, 'home.html', {'notifications': notifications, 'information': information})

def principal_dashboard(request):
    if 'principal_id' in request.session:
        notifications = Notification.objects.all()
        return render(request, 'principal/dashboard.html', {'notifications': notifications})
    else:
        return redirect('principal_login')

from django.shortcuts import render, redirect
from .models import Notification

def manage_notifications(request):
    if 'principal_id' in request.session:
        if request.method == 'POST':
            title = request.POST.get('title')
            content = request.POST.get('content')
            Notification.objects.create(title=title, content=content)
            return redirect('manage_notifications')
        notifications = Notification.objects.all()
        return render(request, 'principal/manage_notifications.html', {'notifications': notifications})
    else:
        return redirect('principal_login')


def edit_notification(request, notification_id):
    if 'principal_id' in request.session:
        notification = Notification.objects.get(id=notification_id)
        if request.method == 'POST':
            notification.title = request.POST.get('title')
            notification.content = request.POST.get('content')
            notification.save()
            return redirect('manage_notifications')
        return render(request, 'principal/edit_notification.html', {'notification': notification})
    else:
        return redirect('principal_login')

def delete_notification(request, notification_id):
    if 'principal_id' in request.session:
        notification = Notification.objects.get(id=notification_id)
        notification.delete()
        return redirect('manage_notifications')
    else:
        return redirect('principal_login')

def teachers_page(request):
    return render(request, 'teachers_page.html')

def manager_page(request):
    return render(request, 'manager_page.html')



from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def list_students(request):
    if 'principal_id' in request.session:
        students = Student.objects.filter(is_deleted=False)
        return render(request, 'principal/list_students.html', {'students': students})
    else:
        return redirect('principal_login')

def deleted_students(request):
    if 'principal_id' in request.session:
        students = Student.objects.filter(is_deleted=True)
        return render(request, 'principal/deleted_students.html', {'students': students})
    else:
        return redirect('principal_login')

def soft_delete_student(request, student_id):
    if 'principal_id' in request.session:
        student = get_object_or_404(Student, id=student_id)
        student.is_deleted = True
        student.save()
        return redirect('list_students')
    else:
        return redirect('principal_login')

def restore_student(request, student_id):
    if 'principal_id' in request.session:
        student = get_object_or_404(Student, id=student_id)
        student.is_deleted = False
        student.save()
        return redirect('deleted_students')
    else:
        return redirect('principal_login')


def add_student(request):
    if 'principal_id' in request.session:
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            date_of_birth = request.POST.get('date_of_birth')
            admission_date = request.POST.get('admission_date')
            grade = request.POST.get('grade')
            performance = request.POST.get('performance')
            attendance_records = request.POST.get('attendance_records')
            disciplinary_actions = request.POST.get('disciplinary_actions')
            total_fee = request.POST.get('total_fee')
            remaining_fee = request.POST.get('remaining_fee')
            attendance_percentage = request.POST.get('attendance_percentage')
            Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                admission_date=admission_date,
                grade=grade,
                performance=performance,
                attendance_records=attendance_records,
                disciplinary_actions=disciplinary_actions,
                total_fee=total_fee,
                remaining_fee=remaining_fee,
                attendance_percentage=attendance_percentage
            )
            return redirect('list_students')
        return render(request, 'principal/add_student.html')
    else:
        return redirect('principal_login')

def edit_student(request, student_id):
    if 'principal_id' in request.session:
        student = get_object_or_404(Student, id=student_id)
        if request.method == 'POST':
            student.first_name = request.POST.get('first_name')
            student.last_name = request.POST.get('last_name')
            student.date_of_birth = request.POST.get('date_of_birth')
            student.admission_date = request.POST.get('admission_date')
            student.grade = request.POST.get('grade')
            student.performance = request.POST.get('performance')
            student.attendance_records = request.POST.get('attendance_records')
            student.disciplinary_actions = request.POST.get('disciplinary_actions')
            student.total_fee = request.POST.get('total_fee')
            student.remaining_fee = request.POST.get('remaining_fee')
            student.attendance_percentage = request.POST.get('attendance_percentage')
            student.save()
            return redirect('list_students')
        return render(request, 'principal/edit_student.html', {'student': student})
    else:
        return redirect('principal_login')

def delete_student(request, student_id):
    if 'principal_id' in request.session:
        student = get_object_or_404(Student, id=student_id)
        student.delete()
        return redirect('list_students')
    else:
        return redirect('principal_login')


from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout

def logout_view(request):
    if 'principal_id' in request.session:
        del request.session['principal_id']
    return redirect('home_page')



from django.shortcuts import render, redirect
from .models import Teacher
from django.contrib.auth.hashers import check_password, make_password

def teacher_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            teacher = Teacher.objects.get(username=username)
            if check_password(password, teacher.password):
                request.session['teacher_id'] = teacher.id
                return redirect('teachers_dashboard')  # Assuming you have a dashboard view for teachers
            else:
                error_message = 'Invalid username or password'
        except Teacher.DoesNotExist:
            error_message = 'Invalid username or password'
        
        return render(request, 'teacher/login.html', {'error_message': error_message})
    else:
        return render(request, 'teacher/login.html')

def teachers_dashboard(request):
    if 'teacher_id' in request.session:
        # Fetch any required data for teachers dashboard here
        return render(request, 'teacher/dashboard.html')
    else:
        return redirect('teacher_login')



from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import Teacher

def add_teacher(request):
    if 'principal_id' in request.session:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            name = request.POST.get('name')
            email = request.POST.get('email')
            if username and password and name and email:
                Teacher.objects.create(
                    username=username,
                    password=make_password(password),
                    name=name,
                    email=email
                )
                return redirect('principal_dashboard')
            else:
                error_message = 'All fields are required.'
                return render(request, 'principal/add_teacher.html', {'error_message': error_message})
        else:
            return render(request, 'principal/add_teacher.html')
    else:
        return redirect('principal_login')
