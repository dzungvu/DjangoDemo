from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class LoginView(APIView):
    def get(self, request):
        content = {
            'username': 'taolao',
            'is_register': True
        }

        return Response(data=content, status=status.HTTP_200_OK)
