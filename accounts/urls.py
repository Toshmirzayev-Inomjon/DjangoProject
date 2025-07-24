from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView
from accounts.views import logged_out,dashboard_views

urlpatterns = [
    # path('login/',user_login, name='login')
    path('',LoginView.as_view(), name='login'),
    path('chiqish/',logged_out,name='logged_out'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_cange_done'),
    path('profil/',dashboard_views,name='profil'),

]