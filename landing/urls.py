from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
app_name='landing'
urlpatterns=[
    path('',views.HomeView.as_view(),name='home'),
    path('welcome/',login_required(views.WelcomeView.as_view()),name='welcome')
]