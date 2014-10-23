from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rocketu_blog_analytics import settings

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^blog/$', 'blog.views.blog', name='blog'),
    url(r'^blog/(\d+)/$', 'blog.views.post', name='post'),
    url(r'^tag/(\d+)/$', 'blog.views.tag', name='tags'),
    url(r'^error/$', 'blog.views.error', name='error'),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
