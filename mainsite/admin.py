from django.contrib import admin
from mainsite.models import Post, carManufacture, carModels

# Register your models here.


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'pub_date')

	
admin.site.register(Post, PostAdmin)
admin.site.register(carManufacture)
admin.site.register(carModels)
