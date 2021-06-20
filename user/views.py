from django.http.response import Http404,HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import get_user_model

from .forms import UsereditForm
# Create your views here.

User  =get_user_model()


class ProfileView(View):
    template_name_auth = 'user/profile_auth.html'
    template_name_anon = 'user/profile_anon.html'

    def get(self,request,*args,**kwargs):
        username= kwargs.get('username')
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            return HttpResponse('<h1>This User does not exist.</h1>')
        context = {
            'user': user
        }
        return render(request,self.template_name_auth,context)


class ProfileeditView(View):
    template_name = 'user/edit_profile.html'

    form_class = UsereditForm

    def get(self,request,*args,**kwargs):
        username = kwargs.get('username')

        if username != request.user.username:
            return HttpResponse('<h1>You have no autority to access this page</h1>')

        form = self.form_class(instance=request.user)
        context = {
            'form':form
        }
        return render(request,self.template_name,context=context)

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST,request.FILES,instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('Profile_view',request.user.username)

        context = {'form': form}
        return render(request, self.template_name, context=context)