from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/', include('api.urls', namespace='api')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('workout_plan/', include(('workout_plan.urls', 'workout_plan'), namespace='workout_plan')),
    path('text_recognition/', include(('text_recognition.urls', 'text_recognition'), namespace='text_recognition')),
    path('login/', views.obtain_auth_token, name='login'),
]