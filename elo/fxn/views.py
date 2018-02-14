from django.views.generic import TemplateView
from.forms import MemberForm
from .models import BucxMember
from django.shortcuts import render, redirect
from allauth.account.models import EmailAddress

class HomePage(TemplateView):
    template_name = 'account/base.html'

class AccountSettingPage(TemplateView):
    template_name = 'account/acc_sett.html'

def CreateProfile(request):
    #if request.user.is_authenticated():
            form = MemberForm(request.method == 'POST')
        #if form.is_valid():
#            email = form.cleaned_data["e_mail"]
#            result = EmailAddress.objects.filter(email=self.user.email)
#            if email!=result:
#                return redirect('fxn:home')
            instance = form.save(commit=False)
            instance.user =request.user
            instance.save()
            context = {
                "form":form,
            }
            return render(request,"member_form.html",context)
    #else:

        #return redirect('fxn:home')
