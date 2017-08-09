from django.http import HttpResponse

def index(request):
	return HttpResponse("My staticpages homepage.")

def about_page_view(request):
	return HttpResponse("About page.")