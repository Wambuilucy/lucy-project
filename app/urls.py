from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^index/$',views.index,name='index'),
    url('^about/$',views.about,name = 'about'), 
    url('^base/$',views.base,name='base'),
    url('^navbar/$',views.navbar,name='navbar'),
    url('^contribute/$',views.contribute,name = 'contribute'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)