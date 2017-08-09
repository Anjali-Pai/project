from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
	#return render(request,'app/index.html')

#def about_page_view(request):
 #   return render(request, 'app/about.html')


from django.views.generic import TemplateView
class Index(TemplateView):
    template_name = "app/index.html"
class About_page_view(TemplateView):
    template_name = "app/about.html"