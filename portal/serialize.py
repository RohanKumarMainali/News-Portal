from rest_framework import serializers
from .models import *

class BlogSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)  
    class Meta:
        model=Blog
        fields="__all__"