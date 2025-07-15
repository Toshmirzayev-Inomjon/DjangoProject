from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .forms import ContactForm
from .models import News, Category


def home_view(request):
    news = News.published.all()
    category = Category.objects.all()
    news_object_one = News.published.order_by('publish_time')[0]
    home_news = News.published.order_by('-publish_time')[:3]
    news_4 = News.published.order_by('-publish_time')[:4]
    context = {
        'news':news,
        "category":category,
        "news_object_one":news_object_one,
        "home_news":home_news,
        "news_4": news_4

    }
    return render(request,'index.html', context= context)

def category_page(request):
    news = News.published.order_by('-publish_time')[1:5]
    news1 = News.published.order_by('-publish_time')[5:10]
    news2 = News.published.order_by('-publish_time')[10:15]
    news3 = News.published.order_by('-publish_time')[15:20]
    news4 = News.published.order_by('-publish_time')[25:30]
    news5 = News.published.order_by('-publish_time')[35:40]
    category = Category.objects.all()
    context = {
        'news': news,
        'news1': news1,
        'news2': news2,
        'news3': news3,
        'news4': news4,
        'news5': news5,
        "category": category,
    }
    return render(request, 'categori.html', context=context)




def news_detail(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Published)
    context = {
        'news':news,
    }
    return render(request, 'detail.html', context= context)

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
            return HttpResponse('HABAR INOMJONGA YUBORILDI')
        context = {
            'form':form
        }

        return render(request, 'contact.html', context= context)


