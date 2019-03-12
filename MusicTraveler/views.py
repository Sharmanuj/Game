from django.shortcuts import render,redirect,reverse,HttpResponse,HttpResponseRedirect
from django import views
def home(request):
    return render(request,'home.html')

class HomeView(views.generic.TemplateView):
    template_name='home.html'
