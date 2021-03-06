"""demobot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test, login_required
from django.urls import path, include
from app import views
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.views import LogoutView

urlpatterns = [
  # path('admin/', admin.site.urls),
  # path('api/', include(router.urls))
  path('', staff_member_required(TemplateView.as_view(template_name='index.html'))),
  path('', login_required(TemplateView.as_view(template_name='index.html'))),
  # path('',user_passes_test(lambda u:u.is_staff, login_url=TemplateView.as_view(template_name='index.html'))),
  # path('',  TemplateView.as_view(template_name='index.html')),
  path('api/', include('app.urls')),
  path('', include('app.urls')),
  # url(r'^$',
  #   TemplateView.as_view(template_name='index.html'),
  #  name='uHome'
  # ),
  url('dashboard/', staff_member_required(TemplateView.as_view(template_name='index.html')), name='dashboard'),
  url(r'^logout/$', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
  url(r'^admin/', admin.site.urls),
  # url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
  #    url(r'^api/group', views.GroupViewSet.as_view()),

]
# urlpatterns += staticfiles_urlpatterns()
admin.site.site_header = "J'arrete de fumer - Help Admin"
admin.site.site_title = "J'arrete de fumer Admin Portal"
admin.site.index_title = "Welcome to J'arrete de fumer Portal"
