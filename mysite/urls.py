from django.conf.urls import patterns, include, url

from django.contrib import admin
from crawlingData import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.main_page,name='main_page'),
    url(r'^admin/', include(admin.site.urls)),
)
