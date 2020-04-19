from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .authentication import UserAuthentication
from rest_framework.permissions import IsAuthenticated
import json
from django.contrib.auth import login


# Create your views here.
class LoginView(APIView):
    authentication_classes = (UserAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):

        login(request, request.user, backend='user.authentication.UserAuthentication')

        return super(LoginView, self).post(request, format=None)
