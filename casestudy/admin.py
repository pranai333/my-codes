from django.contrib import admin
from .models import questions

# Register your models here.
class questionsadmin(admin.ModelAdmin):
    list_display=['text','option1','option2','option3','option4','correct_answer']
    #list_editable=['text','option1','option2','option3','option4','correct_answer']
    list_display_links=None
admin.site.register(questions,questionsadmin),
