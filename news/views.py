from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .forms import ContactForm
from .models import News, Category, User, Blog, Blog_Category


def home_view(request):
    news = News.published.all()
    category = Category.objects.all()
    news_object_one = News.published.order_by('publish_time')[0]
    home_news = News.published.order_by('-publish_time')[:3]
    news_4 = News.published.order_by('-publish_time')[:5]
    news_10 = News.published.order_by('-publish_time')[:10]
    context = {
        "news":news,
        "category":category,
        "news_10":news_10,
        "news_object_one":news_object_one,
        "home_news":home_news,
        "news_4": news_4

    }
    return render(request,'index.html', context= context)

def single_blog_page(request, id):
    blog = get_object_or_404(Blog, id=id, status=Blog.Status.Published)
    context = {
        'blog':blog
    }
    return render(request, 'single-blog.html', context=context)

def blog_page(request):
    news = News.published.all()
    context = {

    }
    return render(request, 'blog.html', context=context)

def latest_news_page(request):
    news = News.published.all()
    context = {

    }
    return render(request, 'latest_news.html', context=context)

def about_page(request):
    news = News.published.all()
    context = {
        'news':news
    }
    return render(request, 'about.html', context=context)

def category_page(request):
    news = News.published.order_by('publish_time')
    category = Category.objects.all()
    paginator = Paginator(news, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'news': page_obj.object_list,
        'page_obj':page_obj,
        "category": category,
    }
    return render(request, 'categori.html', context=context)




def news_detail(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Published)
    new = News.published.all()
    context = {
        'news':news,
        'new':new
    }
    return render(request, 'details.html', context= context)

class ContactPageView(TemplateView):
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
                'form':form
            }
        return render(request, 'contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST )
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse('Successfully submitted')
        context = {
            'form':form
        }

        return render(request, 'contact.html', context= context)


