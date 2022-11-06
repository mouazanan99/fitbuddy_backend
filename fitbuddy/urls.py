from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/', include('api.urls', namespace='api')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('login/', views.obtain_auth_token, name='login'),
]