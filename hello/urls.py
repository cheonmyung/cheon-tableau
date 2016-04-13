"""hello URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls.static import static

#from tableau.views import TableauHomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^posts/', include("tableau.urls")),
    #url(r'^$', TableauHomeView.as_view()),
    url(r'^$', 'tableau.views.home_page', name='home_page'),

    # About_me page
    url(r'^about/$', 'tableau.views.about_me', name='about_me'),




    # Post a Tableau!
    url(r'^create/$', "tableau.views.post_create", name='create'),



    # ----------- Industries ----------- #

    # Retail Industry
    url(r'^retail/$', "tableau.views.post_list", name='list'),

    url(r'^retail/(?P<slug>[\w-]+)/$', "tableau.views.post_detail", name='detail'),
    url(r'^retail/(?P<slug>[\w-]+)/edit/$', "tableau.views.post_update", name='update'),
    url(r'^retail/(?P<slug>[\w-]+)/delete/$', "tableau.views.post_delete", name='delete'),


    # Banking Industry

    #url(r'^banking_create/$', "tableau.views.banking_create", name='banking_create'),

    url(r'^banking/$', "tableau.views.banking_list", name='banking_list'),

    url(r'^banking/(?P<slug>[\w-]+)/$', "tableau.views.banking_detail", name='banking_detail'),
    url(r'^banking/(?P<slug>[\w-]+)/edit/$', "tableau.views.banking_update", name='banking_update'),
    url(r'^banking/(?P<slug>[\w-]+)/delete/$', "tableau.views.banking_delete", name='banking_delete'),

    # Social Network Industry

    url(r'^social_network/$', "tableau.views.social_list", name='social_list'),

    url(r'^social_network/(?P<slug>[\w-]+)/$', "tableau.views.social_detail", name='social_detail'),
    url(r'^social_network/(?P<slug>[\w-]+)/edit/$', "tableau.views.social_update", name='social_update'),
    url(r'^social_network/(?P<slug>[\w-]+)/delete/$', "tableau.views.social_delete", name='social_delete'),


    # Real Estate Industry

    url(r'^real_estate/$', "tableau.views.real_list", name='real_list'),
    url(r'^real_estate/(?P<slug>[\w-]+)/$', "tableau.views.real_detail", name='real_detail'),
    url(r'^real_estate/(?P<slug>[\w-]+)/edit/$', "tableau.views.real_update", name='real_update'),
    url(r'^real_estate/(?P<slug>[\w-]+)/delete/$', "tableau.views.real_delete", name='real_delete'),


    # Travel Industry

    url(r'^travel/$', "tableau.views.travel_list", name='travel_list'),
    url(r'^travel/(?P<slug>[\w-]+)/$', "tableau.views.travel_detail", name='travel_detail'),
    url(r'^travel/(?P<slug>[\w-]+)/edit/$', "tableau.views.travel_update", name='travel_update'),
    url(r'^travel/(?P<slug>[\w-]+)/delete/$', "tableau.views.travel_delete", name='travel_delete'),


    # HealthCare Industry

    url(r'^healthcare/$', "tableau.views.health_list", name='health_list'),
    url(r'^healthcare/(?P<slug>[\w-]+)/$', "tableau.views.health_detail", name='health_detail'),
    url(r'^healthcare/(?P<slug>[\w-]+)/edit/$', "tableau.views.health_update", name='health_update'),
    url(r'^healthcare/(?P<slug>[\w-]+)/delete/$', "tableau.views.health_delete", name='health_delete'),




    ## ------------------------ Blog Types ----------------------------- ##

    url(r'^blog_create/$', "tips.views.blog_create", name='blog_create'),

    # Basic Steps 

    url(r'^basic/$', "tips.views.basic_list", name='basic_list'),
    url(r'^basic/(?P<slug>[\w-]+)/$', "tips.views.basic_detail", name='basic_detail'),
    url(r'^basic/(?P<slug>[\w-]+)/edit/$', "tips.views.basic_update", name='basic_update'),
    url(r'^basic/(?P<slug>[\w-]+)/delete/$', "tips.views.basic_delete", name='basic_delete'),


    # Tableau Concepts 

    url(r'^concepts/$', "tips.views.concepts_list", name='concepts_list'),
    url(r'^concepts/(?P<slug>[\w-]+)/$', "tips.views.concepts_detail", name='concepts_detail'),
    url(r'^concepts/(?P<slug>[\w-]+)/edit/$', "tips.views.concepts_update", name='concepts_update'),
    url(r'^concepts/(?P<slug>[\w-]+)/delete/$', "tips.views.concepts_delete", name='concepts_delete'),


    # Simple Techniques 

    url(r'^techniques/$', "tips.views.techniques_list", name='techniques_list'),
    url(r'^techniques/(?P<slug>[\w-]+)/$', "tips.views.techniques_detail", name='techniques_detail'),
    url(r'^techniques/(?P<slug>[\w-]+)/edit/$', "tips.views.techniques_update", name='techniques_update'),
    url(r'^techniques/(?P<slug>[\w-]+)/delete/$', "tips.views.techniques_delete", name='techniques_delete'),



    # Tableau Desktop  

    url(r'^desktop/$', "tips.views.desktop_list", name='desktop_list'),
    url(r'^desktop/(?P<slug>[\w-]+)/$', "tips.views.desktop_detail", name='desktop_detail'),
    url(r'^desktop/(?P<slug>[\w-]+)/edit/$', "tips.views.desktop_update", name='desktop_update'),
    url(r'^desktop/(?P<slug>[\w-]+)/delete/$', "tips.views.desktop_delete", name='desktop_delete'),



    # Tips   

    url(r'^tips/$', "tips.views.tips_list", name='tips_list'),
    url(r'^tips/(?P<slug>[\w-]+)/$', "tips.views.tips_detail", name='tips_detail'),
    url(r'^tips/(?P<slug>[\w-]+)/edit/$', "tips.views.tips_update", name='tips_update'),
    url(r'^tips/(?P<slug>[\w-]+)/delete/$', "tips.views.tips_delete", name='tips_delete')





    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

