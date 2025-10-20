from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


class EmailBackend(ModelBackend):
    """
    Custom authentication backend that lets users log in using their email
    instead of username.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Try to find a user with the given email
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        # Check if the password is correct
        if user.check_password(password):
            return user

        # Return none if authentication fails
        return None
