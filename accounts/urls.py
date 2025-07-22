from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from accounts.views import logged_out

urlpatterns = [
    # path('login/',user_login, name='login')
    path('',LoginView.as_view(), name='login'),
    path('chiqish/',logged_out,name='logged_out')
]