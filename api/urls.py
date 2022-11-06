from django.urls import path
from .views import UserRecordView, UserProfileView, UserFitnessView

app_name = 'api'
urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
    path('userProfile/', UserProfileView.as_view(), name='userProfile'),
    path('userFitness/', UserFitnessView.as_view(), name='userFitness'),
]