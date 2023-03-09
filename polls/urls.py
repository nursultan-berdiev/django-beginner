from django.urls import path, include

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.Index.as_view(), name='index'),

    # path('<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.QuestionDetail.as_view(), name='detail'),

    # path('<int:question_id>/result/', views.result, name='result'),
    path('<int:question_id>/result/', views.Result.as_view(), name='result'),

    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/vote/', views.Vote.as_view(), name='vote'),
]
