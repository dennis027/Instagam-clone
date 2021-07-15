from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^new/post', views.new_post, name='new-post'),
    # url(r'^search/', views.search_results, name='search_results'),
    # url(r'^new/welcome$', views.welcome, name='new-post'),
    url(r'^accounts/profile/$',views.profile,name = 'profile'),
    url(r'^profile/(\d+)',views.other_profile,name = 'visitprofile'),
    url(r'^search/profile$', views.search, name='search_results'),
    url(r'^edit_profile$', views.edit_profile, name='edit'),
    url(r'^new/post', views.post_detail, name='post_detail'),
    url('<slug:slug>/', views.post_detail, name='post_detail')
  
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
