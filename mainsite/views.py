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
	

def convert(request, num, unit):
	templates = get_template('converion.html')
	if unit == 'cm':
		converted = str(int(num)*0.3937) + ' in'
	elif unit == 'in' or 'inch' or 'inches':
		converted = str(int(num)*2.54) + ' cm'
	html = templates.render(locals())
	return HttpResponse(html)