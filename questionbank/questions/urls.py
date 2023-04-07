from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('questions/', views.QuestionListView.as_view(), name='question-list'),
    path('questions/search', views.SearchQuestionListView.as_view(),
         name='search-results'),
    path('question/<int:pk>/', views.QuestionDetailView.as_view(),
         name='question-detail'),
    path('exams/', views.ExamListView.as_view(), name='exam-list'),
    path('exam/<int:pk>/', views.ExamDetailView.as_view(),
         name='exam-detail'),
]
