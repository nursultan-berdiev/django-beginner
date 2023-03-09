from django.contrib import admin

from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date']


admin.site.register(Question, QuestionAdmin)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question', 'choice_text', 'votes']
    search_fields = ['choice_text', 'question__question_text']
