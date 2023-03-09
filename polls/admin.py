from django.contrib import admin

from .models import Question, Choice

admin.site.register(Question)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question', 'choice_text', 'votes']
    search_fields = ['choice_text', 'question__question_text']
