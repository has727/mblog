from django.shortcuts import render, HttpResponse
from .models import Post
from django.template.loader import get_template
from datetime import datetime

# Create your views here.


def homepage(request):
	templates = get_template('index.html')
	posts = Post.objects.all()
	now = datetime.now
	html = templates.render(locals())
	return HttpResponse(html)