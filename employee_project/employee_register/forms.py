from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model=Employee
        fields = ('name', 'email', 'address', 'phone')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }