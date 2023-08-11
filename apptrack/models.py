from django.db import models

# Create your models here.
BOOL=(
    ('Yes','Yes'),
    ('No','No'),
)
class EmployeeAdd(models.Model):
    name=models.CharField(max_length=200)
    device_type=models.CharField(max_length=200)
    device_name=models.CharField(max_length=200)
    device_number=models.IntegerField()
    handle_on=models.CharField(choices=BOOL, max_length=50)
    handle_date=models.DateField()
    return_on=models.CharField(choices=BOOL, max_length=50)
   
    class Meta:
        verbose_name = "EmployeeAdd"
        verbose_name_plural = "EmployeeAdd" 

SELECT=(
    ('Yes','Yes'),
    ('No','No'),
)
class Employee(models.Model):
    name=models.CharField(max_length=200)
    device_type=models.CharField(max_length=200)
    device_name=models.CharField(max_length=200)
    device_number=models.IntegerField()
    given=models.CharField(choices=SELECT, max_length=50)
    given_date=models.DateField()
    returned=models.CharField(choices=SELECT, max_length=50)
    returned_date=models.TextField(max_length=200)
   
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employee"   



class Device(models.Model):
    details=models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='device_details')
    class Meta:
        verbose_name = "Device"
        verbose_name_plural = "Device" 
