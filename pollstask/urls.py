from django.urls import path, include
from pollstask.views import *
from pollstask import views

urlpatterns = [
    path('pollslist/', PollsListAllView.as_view()),
    path('polls/', PollsListView.as_view()),
    path('polls/detail/<int:pk>', PollsDetailView.as_view()),
    path('questions/', QuestionsView.as_view()),
    path('questions/detail/<int:pk>', QuestionsDetailView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('choices/', ChoiceView.as_view()),
    path('choice/detail/<int:pk>', ChoiceDetailView.as_view()),
    path('answers/', AnswersView.as_view()),
    path('answer/detail/<int:pk>', AnswerDetailView.as_view()),
]