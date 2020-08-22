from django.urls import path
from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView

app_name = 'weatherapp'
urlpatterns = [
    path('', views.index, name='index'),
    # path('',
    #     TemplateView.as_view(template_name="index.html"),
    #     name="app",
    # )
]