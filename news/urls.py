from django.urls import path

import news.views
from . import views
from .views import home_view, CreateNewsView

urlpatterns = [
    path('', home_view, name='home_page'),
    path('create/',CreateNewsView.as_view(), name='create_news'),
    path('about/', views.about_page, name='about_page'),
    path('contact/', views.ContactPageView.as_view(), name='contact_page'),
    path('category/', views.category_page, name='category_page'),
    path('uzbekistan/', views.uzbekistan_news, name='uzbekistan_page'),
    path('jahon/', views.world_news, name='jahon_page'),
    path('iqtisodiyot/', views.iqtisodiyot_news, name='iqtisodiyot_page'),
    path('jamiyat/', views.jamiyat_news, name='jamiyat_page'),
    path('sport/', views.sport_news, name='sport_page'),
    path('fan-texnika/', views.fan_texnika_news, name='fan_texnika_page'),
    path('moliya/', views.moliya_news, name='moliya_page'),
    path('audio/', views.audio_news, name='audio_page'),
    path('talim/', views.talim_news, name='talim_page'),
    path('avto/', views.avto_news, name='avto_page'),
    path('kochmas-mulk/', views.kochmas_mulk_news, name='kochmas_mulk_page'),
    path('soglom-hayot/', views.soglom_hayot_news, name='soglom_hayot_page'),
    path('ayollar-dunyosi/', views.ayollar_dunyosi_news, name='ayollar_dunyosi_page'),
    path('turizm/', views.turizm_news, name='turizm_page'),
    path('isroil-eron/', views.isroil_eron_news, name='isroil_eron_page'),
    path('ukraina-tinchlik/', views.ukraina_tinchlik_news, name='ukraina_tinchlik_page'),
    path('tramp-savdo/', views.tramp_savdo_urushi_news, name='tramp_savdo_page'),
    path('rossiya-ukraina/', views.rossiya_ukraina_news, name='rossiya_ukraina_page'),
    path('biznes.html/', views.biznes_news, name='biznes_page'),
    path('news/<slug>/', views.news_detail, name='news_detail_page'),
    path('news/<slug>/update/',views.UpdateNewsView.as_view(), name='update_news'),
    path('news/<slug>/delete/',views.DeleteNewsView.as_view(), name='delete_news'),
]
