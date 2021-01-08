from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('homepage', views.homepage, name="homepage"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('about', views.about, name="about"),
    path('blog', views.blog, name="blog"),
    path('contact', views.contact, name="contact"),
]