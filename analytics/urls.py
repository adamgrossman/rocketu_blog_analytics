from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rocketu_blog_analytics import settings

urlpatterns = patterns('',
    url(r'^main/$', 'analytics.views.main', name='main'),
    url(r'^view/(\d+)/$', 'analytics.views.view_page', name='view_page'),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
