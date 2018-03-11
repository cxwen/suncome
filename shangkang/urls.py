"""shangkang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from suncome import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index),
    url(r'^index/$',views.index),
    url(r'^yuebing/', TemplateView.as_view(template_name="yuebing/index.htm")),
    url(r'^dangao/', TemplateView.as_view(template_name="dangao/index.htm")),
    url(r'^zongzi/', TemplateView.as_view(template_name="zongzi/index.htm")),
    url(r'^join/', TemplateView.as_view(template_name="join/index.htm")),
    url(r'^about/', TemplateView.as_view(template_name="about/index.htm")),
    url(r'^news/', TemplateView.as_view(template_name="news/index.htm")),
    url(r'^city/', TemplateView.as_view(template_name="city/index.htm")),
]
