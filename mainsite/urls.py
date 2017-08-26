from django.conf.urls import url, include
from django.contrib import admin
from mainsite.views import homepage, showpost


urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', homepage),
	url(r'^post/(.+)/$', showpost),
]
