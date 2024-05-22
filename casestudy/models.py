from django.db import models

# Create your models here.
class user(models.Model):
    user_name=models.CharField(max_length=20)
    user_id=models.IntegerField(primary_key=True)

class questions(models.Model):
    text=models.CharField(max_length=300)
    option1=models.CharField(max_length=70) 
    option2=models.CharField(max_length=70) 
    option3=models.CharField(max_length=70) 
    option4=models.CharField(max_length=70) 
    correct_answer=models.CharField(max_length=50)  