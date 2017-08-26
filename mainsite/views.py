from django.shortcuts import render, HttpResponse, redirect
from .models import Post
from django.template.loader import get_template
from datetime import datetime

# Create your views here.


def homepage(request):
	templates = get_template('index.html')
	posts = Post.objects.all()
	now = datetime.now()
	html = templates.render(locals())
	return HttpResponse(html)


def showpost(request, slug):
	templates = get_template('post.html')
	try:
		post = Post.objects.get(slug=slug)
		if post != None:
			html = templates.render(locals())
			return HttpResponse(html)
	except:
		return redirect('/')
	
	
def index(request, tvno='0'):
	tv_list = [
		{'name': 'Panzer II', 'tvcode': 'd5ZdYKU2dyo'},
		{'name': 'German Wiesel', 'tvcode': 'oPgDLhyRgaM'},
	]
	templates = get_template('tv.html')
	now = datetime.now()
	tvno = tvno
	tv = tv_list[int(tvno)]
	html = templates.render(locals())
	return HttpResponse(html)
	