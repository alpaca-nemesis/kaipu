#coding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'crowix.views.index'),
    url(r'^index/', 'crowix.views.index', name='index'),
    url(r'^login/', 'crowix.views.login', name='login'),
    url(r'^logout/', 'crowix.views.logout', name='logout'),
    url(r'^regist/', 'crowix.views.regist', name='regist'),
    url(r'^contact/', 'crowix.views.contact', name='contact'),
    url(r'^message/', 'crowix.views.message', name='message'),
    url(r'^product/$', 'crowix.views.product_page',name='product'),
    url(r'^products/(\d+)/', 'crowix.views.product_pages',name='products'),
    url(r'^profile/', 'crowix.views.profile_page',name='profile'),
    url(r'^video/', 'crowix.views.video_page',name='video'),
    url(r'^news/', 'crowix.views.news_page',name='news'),      
    url(r'^certif/', 'crowix.views.certif_page',name='certif'),          
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
)