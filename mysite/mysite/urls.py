"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from companies import views
from mysite.views import hello, current_datetime, hours_ahead

urlpatterns = [
	url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^blogs/', include('blog.urls')),
    url(r'^blogs2/', include('blog2.urls')),
    url(r'^music/', include('music.urls')),
    url(r'^stocks/', views.StockList.as_view()),
    url(r'^hello/$', hello), 
    url(r'^time/$', current_datetime), 
    url(r'^time/plus/(\d{1,2})/$', hours_ahead)

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
