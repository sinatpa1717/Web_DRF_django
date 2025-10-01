from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import seria_page_profile_user
from .models import profile_user_model
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class page_web_profile_user(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        profile = request.user.profile
        serial = seria_page_profile_user(profile)
        return Response(serial.data)