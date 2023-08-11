import django
from django.contrib.auth import models
from django.core import validators
from django import forms
from django.forms import fields, widgets
from django import forms

#django form create kore bellow models and forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import *

class Create(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2' ]

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=EmployeeAdd
        fields=['name','device_type','device_name','device_number','handle_on','handle_date','return_on']

class EmployeeAddForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['name','device_type','device_name','device_number','given','given_date','returned','returned_date']

class DeviceForm(forms.ModelForm):
  
    class Meta:
        model = Device
        fields = ['details']

    def __init__(self, *args, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'           