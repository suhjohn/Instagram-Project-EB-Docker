from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static


urlpatterns = [
    url(r'^post/', include('post.urls.apis', namespace='api-post')),
    url(r'^member/', include('member.urls.apis', namespace='api-member')),
]
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
