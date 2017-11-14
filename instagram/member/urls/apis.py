from django.conf.urls import url

from ..apis import Signup, Login

urlpatterns = [
    url(r'^login/$', Login.as_view(), name='api-login'),
    url(r'^signup/$', Signup.as_view(), name='api-signup'),
]
