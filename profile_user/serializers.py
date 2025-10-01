from .models import profile_user_model
from rest_framework import serializers

class seria_page_profile_user(serializers.ModelSerializer):
    
    class Meta:
        model = profile_user_model
        fields = "__all__"