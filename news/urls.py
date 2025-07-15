from django.urls import path

from news.views import news_detail, ContactPageView, home_view, category_page

urlpatterns = [
    path('', home_view, name='home_page'),
    path('<int:id>/', news_detail, name='news_detail_page'),
    path('contact.html/', ContactPageView.as_view(), name='contact_page'),
    path('', home_view, name="category_page"),
    path('category.html/', category_page, name='category_page')

]