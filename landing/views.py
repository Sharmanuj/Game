from django.shortcuts import render,redirect,reverse,HttpResponse,HttpResponseRedirect
from django import views

# Create your views here.
class HomeView(views.generic.TemplateView):
    template_name='landing/home.html'


class WelcomeView(views.generic.TemplateView):
    template_name='landing/welcome.html'
