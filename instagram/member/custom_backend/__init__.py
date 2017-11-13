from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from ..models import User
from django.db.models import Q

UserModel = get_user_model()


class UsernameLoginBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            # Try to fetch the user by searching the username or email field
            user = User.objects.get(Q(email=username) | Q(username=username))
            if user.check_password(password) or password == user.password:
                return user

        except User.DoesNotExist:  # Run the default password hasher once to reduce the timing
        # difference between an existing and a non-existing user (#20760).
            User().set_password(password)

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class FacebookBackend(object):
    def authenticate(self, request, facebook_user_id):
        try:
            return User.objects.get(username=f'fb_{facebook_user_id}')
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None