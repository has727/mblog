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
	

def calcs(request, num1, num2):
	templates = get_template('cal.html')
	now = datetime.now()
	sum = int(num1) + int(num2)
	html = templates.render(locals())
	return HttpResponse(html)
