from django.conf.urls import url

from .views import index, about_page_view

urlpatterns = [
    url(r'^$', index),
    url(r'^about', about_page_view),
]