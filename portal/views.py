from django.shortcuts import render

# Create your views here.
from .models import *
from  . import serialize
from .serialize import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from rest_framework import permissions

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))

def blogs(request):
    SingleBlog=Blog.objects.all()
    serializeObj=BlogSerializer(SingleBlog,many='true')
    return Response(serializeObj.data)