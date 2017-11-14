from django.conf.urls import url, include
from django.conf.urls.static import static

from config import settings
from . import apis, views

urlpatterns = [
    url(r'^', include(views)),
    url(r'^api/', include(apis)),

]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
