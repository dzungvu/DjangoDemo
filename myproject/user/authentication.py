from rest_framework.authentication import BasicAuthentication
import json
from .models import User


class UserAuthentication(BasicAuthentication):
    def authenticate(self, request):
        json_data = json.loads(request.body.decode('utf-8'))
        email = json_data.get('email', None)
        try:
            user = User.objects.get(email=email)
            return user

        except User.DoesNotExist:
            print("Login password: no user")
            raise Exception("Email not found. Please sign up for new account.")
