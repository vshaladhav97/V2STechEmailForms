"""custom_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from custom_ui.views import  ManagementTest, ManagementFeatures, TechnologyCategoryView, contact_form, CTA, HireDevopCTC, HiringModel, NewsLetter
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
# from custom_ui.views import MenuNavbarListView, MenuNavbarView, MenuDropdownListView, MenuDropdownView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('_nested_admin/', include('nested_admin.urls')),
    # url(r'^api/MenuNavbar/$', MenuNavbarListView.as_view()),
    # url(r'^api/MenuNavbar/(?P<pk>\d+)/$', MenuNavbarView.as_view()),
    # url(r'^api/MenuDropdown/$', MenuDropdownListView.as_view()),
    # url(r'^api/MenuDropdown/(?P<pk>\d+)/$', MenuDropdownView.as_view()),
    # path('', Management.as_view()),
    path('test/', ManagementTest.as_view() ),
    path('features/', ManagementFeatures.as_view()),
    path('technology/', TechnologyCategoryView.as_view()),
    # path('email/', index),
    path('contact-form/', contact_form),
    path('cta/', CTA),
    path('hire-a-developer-cta/', HireDevopCTC),
    path('hiring-model/', HiringModel),
    path('newsletter/', NewsLetter),
    
    
    
        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
