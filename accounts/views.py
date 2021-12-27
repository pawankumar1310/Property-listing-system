from django.http import response
from django.shortcuts import render,HttpResponseRedirect,HttpResponse, redirect, reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .forms import ChangePassword
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from .forms import SignUpForm,LoginForm
from django.views import View
from django.views.generic import CreateView
from Property.models import User,Property_Detail
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView

class Registration(View):
    def get(self,request):
        form = SignUpForm()
        if(request.user.is_authenticated):
            return redirect('/')
        return render(request, 'accounts/register.html', {'form':form})

    def post(self,request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Register Successfully !!')
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect(reverse('home'))



# class Registration(View):
#     def get(self,request):
#         form = SignUpForm()
#         if(request.user.is_authenticated):
#             return redirect('/')
#         return render(request, 'accounts/register.html', {'form':form})

#     def post(self,request):
#         subject = "Thank you for registering to our site"
#         message = "You have successfully created an account"
#         email_from = settings.EMAIL_HOST_USER
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             role = form.cleaned_data.get('role')
#             full_name = form.cleaned_data.get('full_name')
#             email = form.cleaned_data.get('email')
#             recipient_list = ['email',]
#             phone_number = form.cleaned_data.get('phone_number')
#             password = form.cleaned_data.get('password')
#             user = authenticate(email=email,password=password)
#             messages.success(request, 'Register Successfully !!')
#             send_mail(subject,message,email_from,recipient_list)
#             login(request,user)
#             return redirect('/')
#         else:
#             form = SignUpForm()
#         return render(request, 'accounts/register.html', {'form':form})

# class userlogin(LoginView):
#     template_name = 'accounts/login.html'
#     def get(self, request, **kwargs):
#         # If user already logged in redirect home
#         if request.user.is_authenticated:
#             return redirect('/')
#         return super().get(request, **kwargs)


class userlogin(View):
    def get(self,request):
        form = LoginForm()
        if(request.user.is_authenticated):
            return redirect('/')
        return render(request, 'accounts/login.html',{'form':form})

    def post(self,request):
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return render(request,'accounts/login.html',{'error_message': 'Your account has not been activated!'})
            else:
                return render(request,'accounts/login.html', {'error_message': 'Invalid login'})
        return render(request, 'accounts/login.html', {'form':form})


class userlogout(View):
    def logout_user(request):
        logout(request)
        return redirect('all_list')


class PasswordChanged(View):
    def get(self,request):
        form = ChangePassword(user=request.user)
        if(not request.user.is_authenticated):
            return redirect('/')
        return render(request, 'accounts/changepass.html',{'form':form})

    def post(self,request):
        form = ChangePassword(user=request.user,data = request.POST)
        if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,'Password changed Successfully!')
        return render(request,'accounts/changepass.html',{'form':form})



def Dashboard(request):
    properties = Property_Detail.objects.select_related('property').order_by('-created_at')
    context ={
        'contacts':properties
    }
    return render(request,'accounts/dashboard.html',context)


