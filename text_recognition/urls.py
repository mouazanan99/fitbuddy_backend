from .views import QuestionResponseAPI

from django.urls import path

urlpatterns = [
    path('getResponse/', QuestionResponseAPI.as_view(), name='getResponse'),
]