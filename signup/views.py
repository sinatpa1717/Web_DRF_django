from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import serial_signup
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny


# Create your views here.


class page_view_signup(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serial = serial_signup(data=request.data)
        if serial.is_valid():
            user = serial.save()
            token, create = Token.objects.get_or_create(user = user)
            return Response ({
                "username" : serial.data,
                "token" : token.key
            }, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)