from django.conf.urls import url, include
from django.contrib import admin

from ..views import landing_page

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', landing_page, name='landing_page'),
    url(r'^post/', include('post.urls.views', namespace='post')),
    url(r'^member/', include('member.urls.views', namespace='member')),
]
