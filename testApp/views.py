from django.shortcuts import render
from testApp.models import Employee

# Create your views here.
def indexView(request):

    return render(request, 'testApp/index.html')

def empView(request):

    emp_list = Employee.objects.all()
    print(emp_list)
    list = {

        'emp_list' : emp_list
    }
    return render(request, 'testApp/emp.html', context=list)

