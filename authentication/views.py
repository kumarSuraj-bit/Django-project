from django.shortcuts import render,redirect
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

        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin_view')

        context = {'form': form}
        return render(request, self.template_name, context)





class SigninView(View):
    template_name = 'authentication\signin.html'

    def get(self,request,*args,**keargs):
        return render(request,self.template_name)

    def post(self,request,*args,**keargs):
        email_username = request.POST.get('email_username')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(username=email_username)
            email = user_obj.email
        except Exception as e:
            email = email_username

        user = authenticate(request, email=email, password=password)
        
        if user is None:
            messages.error(request, 'Invalid Login.', extra_tags="error")
            return render(request, self.template_name) 

        login(request, user)
        messages.success(request, 'Thanks for Login, Welcome to Insta Clone.', extra_tags='success')
        return redirect('home_feed_view')