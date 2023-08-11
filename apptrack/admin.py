from django.contrib import admin

# Register your models here.
from  .models import *

@admin.register(Device)

class DeviceAdmin(admin.ModelAdmin):
    list_display= ['details']  

@admin.register(EmployeeAdd)

class EmployeeAddAdmin(admin.ModelAdmin):
    list_display= ('name','device_type','device_name','device_number','handle_on','handle_date','return_on')

@admin.register(Employee)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','device_type','device_name','device_number','given','given_date','returned','returned_date')

