from django.conf.urls.defaults import *

from mysite.views import *
from books import views, admin_view

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),
	#url('^$', 'mysite.views.home', name='home'),
	('^hello/$',hello),
	('^time/$', current_datetime),
	(r'^time/plus/(\d{1,2})/$', hours_ahead),
	(r'^search-form/$', views.search_form),
    (r'^search/$', views.search),
	(r'^display/$', views.display_meta),



    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/books/report/$', admin_view.report),
	url(r'^admin/', include(admin.site.urls)),	
)
