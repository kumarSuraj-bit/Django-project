from django.shortcuts import render
from django.views.generic import View
from .forms import UserForm

# Create your views here.

class SignupView(View):
    template_name = 'authentication\signup.html'
    form_class = UserForm

    def get(self,request,*args,**keargs):
        form = self.form_class()
        context = {'form':form}
        return render(request,self.template_name,context=context)

    def post(self,request,*args,**keargs):
        return render(request,self.template_name)





class SigninView(View):
    template_name = 'authentication\signin.html'

    def get(self,request,*args,**keargs):
        return render(request,self.template_name)

    def post(self,request,*args,**keargs):
        return render(request,self.template_name)