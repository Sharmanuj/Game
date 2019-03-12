from django.urls import path,include
from . import views

app_name='room'

urlpatterns=[
    path('',views.CustomerFormView.as_view(),name='room'),
]