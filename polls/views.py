from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


# def index(request):
#     last_question_list = Question.objects.all().order_by('-pub_date')[:5]
#     context = {
#         'questions': last_question_list,
#     }
#     return render(request, 'index.html', context)

class Index(generic.ListView):
    model = Question
    template_name = 'index.html'
    context_object_name = 'questions'

    def get_queryset(self):
        return self.model.objects.all().order_by('pub_date')[:5]


# def detail(request, question_id):
#     # question = Question.objects.get(id=question_id)
#     question = get_object_or_404(Question, id=question_id)
#     return render(request, 'detail.html', {'question': question})

class QuestionDetail(generic.DetailView):
    model = Question


# def result(request, question_id):
#     question = get_object_or_404(Question, id=question_id)
#     return render(request, 'result.html', {'question': question})

class Result(QuestionDetail):
    context_object_name = 'question'
    template_name = 'result.html'
    pk_url_kwarg = 'question_id'


# def vote(request, question_id):
#     question = get_object_or_404(Question, id=question_id)
#     choice_id = int(request.POST.get('choice'))
#     choice = question.choices.get(id=choice_id)
#     choice.votes += 1
#     choice.save()
#     return redirect(reverse('result', kwargs={'question_id': question_id}))


class Vote(generic.View):
    def post(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        choice_id = int(request.POST.get('choice'))
        choice = question.choices.get(id=choice_id)
        choice.votes += 1
        choice.save()
        return redirect(reverse('result', kwargs={'question_id': question_id}))
