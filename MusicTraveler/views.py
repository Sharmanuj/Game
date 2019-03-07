from django.shortcuts import render,redirect,reverse,HttpResponse,HttpResponseRedirect
def home(request):
    return render(request,'home.html')