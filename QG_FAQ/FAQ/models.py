from django.db import models
from django.contrib import admin


# Create your models here.


class Questions(models.Model):
    answer_text = models.CharField(max_length=2000)
    question_text = models.CharField(max_length=2000)

    def __str__(self):
        return self.question_text


@admin.register(Questions)
class CartAdmin(admin.ModelAdmin):
    list_display = ('answer_text', 'question_text')
