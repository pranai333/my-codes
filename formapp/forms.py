from django import forms
from dbapp.models import Employee


class firstforms(forms.Form):
    name=forms.CharField(max_length=20)
    age=forms.IntegerField()

class insertdata(forms.Form):
    empno=forms.IntegerField()
    empname=forms.CharField(max_length=20)
    salary=forms.IntegerField()
    department=forms.IntegerField()

class Modelform(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'