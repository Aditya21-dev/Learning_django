from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializers
from .models import User

# Create your views here.
@api_view(['GET', 'POST'])
def User_list(req):
    if req.method=='POST':
        serializer =    UserSerializers(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    stu = User.objects.all()
    serializer = UserSerializers(stu, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT','PATCH','DELETE'])
def details(req,pk):
    pass