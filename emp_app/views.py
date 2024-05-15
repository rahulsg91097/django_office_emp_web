from django.shortcuts import render, HttpResponse
from .models import Employee, Department, Role
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'view_all_emp.html', context)

def add_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = request.POST['dept']
        role = request.POST['role']
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id=dept, role_id=role, hired_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee Added Successfully!!")
    elif request.method == "GET":
        return render(request, 'emp_add.html')
    else:
        return HttpResponse("En exception occured! Employee cannot be added")

def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_remove = Employee.objects.get(id=emp_id)
            emp_to_remove.delete()
            return HttpResponse("Employee removed successfully")
        except:
            return HttpResponse("Please enter valid id")
    
    emps = Employee.objects.all()
    context = {
        "emps": emps
    }
    return render(request, 'emp_remove.html', context)

def filter_emp(request):
    return render(request, 'emp_filter.html')