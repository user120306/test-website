"""todo URL Configuration

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
from app.views import home
from app.views import todo
from django.contrib import admin
import os.path

admin.autodiscover()

site_media = os.path.join(os.path.dirname(__file__), 'site_media')

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', home.main_page),
	url(r'^signup$', home.signup),
	url(r'^login$', home.login),
	url(r'^logout$', home.logout),
	url(r'^add-todo$', todo.add_todo),
	url(r'^edit-todo/(?P<todo_id>\d+)$', todo.edit_todo),
	url(r'^delete-todo/(?P<todo_id>\d+)$', todo.delete_todo),
	url(r'^edit-user/(?P<pk>\d+)$', home.edit_user),

]
