from encodings.punycode import selective_len, selective_find

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from django.core.paginator import Paginator

from .forms import ContactForm
from .models import News, Category


def home_view(request):
    news = News.published.all()
    category = Category.objects.all()
    news_object_one = News.published.order_by('publish_time').first()
    home_news = News.published.order_by('-publish_time')[:3]
    news_4 = News.published.order_by('-publish_time')[:5]
    news_10 = News.published.order_by('-publish_time')[:10]

    context = {
        "news": news,
        "category": category,
        "news_10": news_10,
        "news_object_one": news_object_one,
        "home_news": home_news,
        "news_4": news_4,
    }
    return render(request, 'index.html', context)


def about_page(request):
    news = News.published.all()
    return render(request, 'about.html', {'news': news})


def category_page(request):
    news = News.published.order_by('publish_time')
    category = Category.objects.all()
    paginator = Paginator(news, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'news': page_obj.object_list,
        'page_obj': page_obj,
        "category": category,
    }
    return render(request, 'categori.html', context)


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug, status=News.Status.Published)
    new = News.published.all()

    return render(request, 'details.html', {'news': news, 'new': new})



class ContactPageView(TemplateView):
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Successfully submitted')
        return render(request, 'contact.html', {'form': form})


class HomePageView(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = News.published.all()
        context['categories'] = Category.objects.all()
        context['world_news'] = News.published.filter(category__name__iexact='Jahon').order_by('-publish_time')
        return context




def uzbekistan_news(request):
    news = News.published.filter(category__name__iexact="uzbekistan")
    return render(request, 'uzbekistan.html', {'news': news})


def world_news(request):
    news = News.published.filter(category__name__iexact="Jahon")
    return render(request, 'jahon.html', {'news': news})

def biznes_news(request):
    news = News.published.filter(category__name__iexact="biznes")
    return render(request, 'biznes.html', {'news': news})


def iqtisodiyot_news(request):
    news = News.published.filter(category__name__iexact="Iqtisodiyot")
    return render(request, 'iqtisodiyot.html', {'news': news})


def jamiyat_news(request):
    news = News.published.filter(category__name__iexact="Jamiyat")
    return render(request, 'jamiyat.html', {'news': news})


def sport_news(request):
    news = News.published.filter(category__name__iexact="Sport")
    return render(request, 'sport.html', {'news': news})


def fan_texnika_news(request):
    news = News.published.filter(category__name__iexact="Fan-texnika")
    return render(request, 'fan_texnika.html', {'news': news})


def moliya_news(request):
    news = News.published.filter(category__name__iexact="Moliya")
    return render(request, 'moliya.html', {'news': news})


def audio_news(request):
    news = News.published.filter(category__name__iexact="Audio")
    return render(request, 'audio.html', {'news': news})


def talim_news(request):
    news = News.published.filter(category__name__iexact="Ta'lim")
    return render(request, 'talim.html', {'news': news})


def avto_news(request):
    news = News.published.filter(category__name__iexact="Avto")
    return render(request, 'avto.html', {'news': news})


def kochmas_mulk_news(request):
    news = News.published.filter(category__name__iexact="Ko‘chmas mulk")
    return render(request, 'kochmas_mulk.html', {'news': news})


def soglom_hayot_news(request):
    news = News.published.filter(category__name__iexact="Soglom hayot")
    return render(request, 'soglom_hayot.html', {'news': news})


def ayollar_dunyosi_news(request):
    news = News.published.filter(category__name__iexact="Ayollar dunyosi")
    return render(request, 'ayollar_dunyosi.html', {'news': news})


def turizm_news(request):
    news = News.published.filter(category__name__iexact="Turizm")
    return render(request, 'turizm.html', {'news': news})


def isroil_eron_news(request):
    news = News.published.filter(category__name__icontains="Isroil")
    return render(request, 'isroil_eron.html', {'news': news})


def ukraina_tinchlik_news(request):
    news = News.published.filter(category__name__icontains="Ukraina")
    return render(request, 'ukraina_tinchlik.html', {'news': news})


def tramp_savdo_urushi_news(request):
    news = News.published.filter(category__name__icontains="Tramp")
    return render(request, 'tramp_savdo.html', {'news': news})


def rossiya_ukraina_news(request):
    news = News.published.filter(category__name__icontains="Rossiya")
    return render(request, 'rossiya_ukraina.html', {'news': news})


class UpdateNewsView(UpdateView):
    model = News
    fields = ('title', 'body', 'image', 'category','status')
    template_name = 'crud/update.html'


class DeleteNewsView(DeleteView):
    model = News
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('home_page')

from django.utils.text import slugify
from django.views.generic.edit import CreateView
from .models import News

class CreateNewsView(CreateView):
    model = News
    template_name = 'crud/create.html'
    fields = ('title', 'body', 'image', 'category', 'status')  # slugni olib tashlaymiz

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)
def form_valid(self, form):
    base_slug = slugify(form.instance.title)
    slug = base_slug
    counter = 1
    while News.objects.filter(slug=slug).exists():
        slug = f'{base_slug}-{counter}'
        counter += 1
    form.instance.slug = slug
    return super().form_valid(form)


