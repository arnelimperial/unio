from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import forms, get_user_model

User = get_user_model()

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Check if the input is an email or username
            if '@' in username:
                user = User.objects.get(email=username)
            else:
                user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        
        # Check password validity
        if user.check_password(password):
            return user
        
        return None