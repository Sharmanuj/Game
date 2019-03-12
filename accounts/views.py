from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import *
from .models import *
from django import views
# Create your views here.
class BecomeHost(PermissionRequiredMixin,views.generic.FormView):
    permission_required='accounts.applied_to_host'
    def has_permission(self):
        if self.request.user.applied_to_host:
            print(self.request.user.username)
            print(self.request.user.applied_to_host)
            return False
        return True
    template_name='accounts/becomehost.html'
    form_class=BecomeHostForm

    def form_valid(self,form):
        print("valid")
        user=get_object_or_404(User,pk=self.request.user.id)
        user.applied_to_host=True
        user.save()
        host=Host(address=form.data.get('address'),country=form.data.get('country'),user=user)
        host.save()
        cc=CreditCardNumber(cc_no=form.data.get('cc_no'),user=user)
        cc.save()
        print(host.address)
        return redirect('landing:welcome')
    
    def form_invalid(self,form):
        print(form.errors)
        return render(self.request,'accounts/becomehost.html',{'form':form})