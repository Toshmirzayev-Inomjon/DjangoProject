from django.shortcuts import render, redirect
from django.template.context_processors import request

from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#
#         if form.is_valid():
#             data = form.cleaned_data
#             user = authenticate(request,
#                                 username=data['username'],
#                                 password=data['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Muffaqiyatli loginqilindi')
#                 else:
#                     HttpResponse('bu username vaqtinchalik activ emas')
#             else:
#                 return HttpResponse('Username yoki parolda xatolik bor')
#     else:
#         form =LoginForm()
#
#     return render(request,'accounts/login.html',{'form':form})

def logged_out(request):
    logout(request)
    return render(request,'registration/logged_out.html')