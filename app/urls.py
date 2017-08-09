from django.conf.urls import url

from .views import Index, About_page_view

#urlpatterns = [
 #   url(r'^$', index),
  #  url(r'^about', about_page_view),
#]

pip
urlpatterns = [
    url(r'^$', Index.as_view()),
     url(r'^about', About_page_view.as_view()),

]