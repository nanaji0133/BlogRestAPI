from django.shortcuts import render
from django.contrib.auth import get_user_model, logout, login

from rest_framework import generics, mixins, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from Accounts.serializers import RegisterSerializer, LoginSerializer, UsersSerializer


User = get_user_model()

# class LoginCreateView(generics.CreateAPIView):
#     serializer_class = LoginCreateSerializer
#     queryset = User.objects.all()
#     permission_classes = [AllowAny]

class RegisterView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save()
            user = User.objects.get(username=serializer.instance.get("username"))
            token = Token.objects.create(user=user)
            return Response({"token":token.key, "user_id":serializer.instance.get("id")}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny,]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data["user"]
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token":token.key, "user_id":user.id}, status=status.HTTP_200_OK)

            # login(request, user)
        #     return Response(serializer.data, status=200)
        # return Response(serializer.errors, status=400)


class LogoutView(APIView):
    def get(self, request):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        # logout(request)
        # return Response(status=200)

class UsersView(generics.ListAPIView):
    serializer_class = UsersSerializer
    queryset = User.objects.all()

