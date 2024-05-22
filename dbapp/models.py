from django.db import models
from django.db.models.signals import pre_save
from django.core.mail import send_mail
from django.conf import settings

# Create your models here.

class Department(models.Model):
    dptno=models.IntegerField(primary_key=True)
    dptname=models.CharField(max_length=20)

    def __str__(self):
        return self.dptname

    
class Employee(models.Model):
    empno=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=20)
    salary=models.IntegerField()
    department=models.ForeignKey(Department,null=True,on_delete=models.SET_NULL)
    images=models.ImageField(upload_to='images/',null=True)

    def __str__(self):
        return self.empname
    
class cars(models.Model):
    regno=models.IntegerField()
    model=models.CharField(max_length=20)

class drivers(models.Model):
    licno=models.IntegerField()
    name=models.CharField(max_length=20)
    car=models.ManyToManyField('cars') 

class books(models.Model):
    bookno=models.IntegerField()
    bookname=models.CharField(max_length=20)

    class Meta:
        abstract=True

class book1(books):
    bookauthor=models.CharField(max_length=20)

class book2(books):
    bookcolour=models.CharField(max_length=20)    

class employeeBooks(Employee):
    class Meta:
        proxy=True
        ordering=['salary']

'''def empsignalhandler(sender,instance,*args,**kwargs):
    #print(sender)
    #print(instance.empname,instance.salary)
    subject='testing email'
    message=
        hi , the data has been inserted to the table , the information
        about the employee his name is {} and salary of {} and his number {}
        .format(instance.empname,instance.salary,instance.empno)
    send_mail(subject=subject,message=message,from_email=settings.EMAIL_HOST_USER,recipient_list=['pranainakka2001@gmail.com'])

pre_save.connect(empsignalhandler,sender=Employee)   '''     