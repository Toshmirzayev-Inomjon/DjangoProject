from django.urls import path

from news import views
from news.views import news_detail, ContactPageView, home_view

urlpatterns = [
    path('', home_view, name='home_page'),
    path('details/<int:id>/', views.news_detail, name='news_detail'),
    path('contact.html/', ContactPageView.as_view(), name='contact_page'),
    path('', home_view, name="category_page"),

]