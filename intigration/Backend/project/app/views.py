from django.shortcuts import render

# Create your views here.


from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

# 🔹 SIGNUP
@api_view(['POST'])
def signup(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )

    return Response({"message": "User created"})


# 🔹 LOGIN
@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    # Django default username use karta hai
    user = authenticate(username=email, password=password)

    if user is None:
        return Response({"message": "Invalid credentials"}, status=400)

    # ✅ JWT Generate
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    res = Response({"message": "Login successful"})

    # ✅ Cookie me store
    res.set_cookie(
        key="token",
        value=access_token,
        httponly=True,
        secure=False,
        samesite='Strict',
        max_age=3600
    )

    return res


# 🔹 PROTECTED HOME
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def home(request):
    return Response({"message": "Welcome Home Sir"})