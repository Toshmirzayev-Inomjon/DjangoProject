from django.urls import path

from news.views import news_detail, ContactPageView, home_view, category_page, single_blog_page, blog_page, \
  about_page, latest_news_page

urlpatterns = [
    path('', home_view, name='home_page'),
    path('<int:id>/', news_detail, name='news_detail_page'),
    path('contact/', ContactPageView.as_view(), name='contact_page'),
    path('category/', category_page, name='category_page'),
    path('blog/<int:id>', single_blog_page, name='single_blog'),
    path('blog/', blog_page, name='blog'),
    path('about/', about_page, name='about'),
    path('latest_news/', latest_news_page, name='latest_news')
]