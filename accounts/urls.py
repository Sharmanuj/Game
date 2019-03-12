from django.conf.urls import url
from django.contrib.auth import views as auth_views, decorators
from django.urls import path
from . import views
app_name='accounts'

urlpatterns=[
    # url(r'^signup',auth_views.LoginView.as_view(),name='signup'),
    # url(r'^login',auth_views.LoginView.as_view(),name='login'),
    path('becomehost',decorators.login_required(views.BecomeHost.as_view()),name='becomehost'),
]