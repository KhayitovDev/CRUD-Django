from django.shortcuts import render, redirect
from .models import *
from .forms import EmployeeForm


def dash(request):
    get_dashboard = Employee.objects.all()
    context = {'get': get_dashboard}
    return render(request, 'employee_register/dashboard.html', context)

def create(request):
    form=EmployeeForm()

    if request.method=='POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'employee_register/forms.html',context )

def update(request, pk):
    project=Employee.objects.get(id=pk)
    form=EmployeeForm( instance=project)

    if request.method=='POST':
        form=EmployeeForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'employee_register/forms.html', context)

def delete (request, pk):
    project=Employee.objects.get(id=pk)
    if request.method=='POST':
        project.delete()
        return redirect('/')
    return render(request, 'employee_register/delete.html', {'object':project})