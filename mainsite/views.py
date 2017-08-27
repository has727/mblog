from django.shortcuts import render, HttpResponse, redirect
from .models import Post, carManufacture, carModels
from django.template.loader import get_template
from datetime import datetime

# Create your views here.


def homepage(request):
	templates = get_template('index.html')
	posts = Post.objects.all()
	now = datetime.now()
	hour = now.time().hour
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
	

def carlist(request, brand_id):
	# car_maker = ['SAAB', 'Ford', 'Honda', 'Mazda', 'Nissan', 'Toyota']
	# car_list = [
	# 	[],
	# 	['Fiesta', 'Focus', 'Modeo', 'EcoSport', 'Kuga', 'Mustang'],
	# 	['Fit', 'Odyssey', 'CR-V', 'City', 'NSX'],
	# 	['Mazda3', 'Mazda5', 'Mazda6', 'CX-3', 'CX-5', 'MX-5'],
	# 	['Tida', 'March', 'Livina', 'Sentra', 'Teana', 'X-Trail', 'Juke', 'Murano'],
	# 	['Camry', 'Altis', 'Yaris', '86', 'Prius', 'Vios', 'RAV4', 'Wish']
	# ]
	
	
	templates = get_template('carlist.html')
	carM = carManufacture.objects.get(id=brand_id)
	carMo = carM.carmodels_set.all()
	
	
	# maker = int(maker)
	# maker_name = car_maker[maker]
	# cars = car_list[maker]
	html = templates.render(locals())
	return HttpResponse(html)