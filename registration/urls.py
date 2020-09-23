from django.urls import path
from registration import views
urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('register/', views.register, name='register'),
]
