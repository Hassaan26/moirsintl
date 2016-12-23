from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    #url(r'^$', 'moirs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('moirsintl.urls')),
    # url(r'^', include('company.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
