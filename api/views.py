from .serializers import UserSerializer, UserProfileSerializer, UserFitnessSerializer
from .models import UserProfile, UserFitness

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User



class UserRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    permission_classes = [IsAdminUser]

    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(
            status= status.HTTP_200_OK,
            data= {
                'status': 0,
                'data': serializer.data
                },
            )

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                status= status.HTTP_201_CREATED,
                data = {
                'status': 1, 
                'data': serializer.data
                },
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class UserProfileView(APIView):

    def get(self, format=None):
        usersProfile = UserProfile.objects.all()
        serializer = UserProfileSerializer(usersProfile, many=True)
        return Response(
            status= status.HTTP_200_OK,
            data= {
                'status': 0,
                'data': serializer.data
                },
            )

    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                status= status.HTTP_201_CREATED,
                data = {
                'status': 1, 
                'data': serializer.data
                },
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class UserFitnessView(APIView):

    def get(self, format=None):
        usersFitness = UserFitness.objects.all()
        serializer = UserFitnessSerializer(usersFitness, many=True)
        return Response(
            status= status.HTTP_200_OK,
            data= {
                'status': 0,
                'data': serializer.data
                },
            )

    def post(self, request):
        serializer = UserFitnessSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                status= status.HTTP_201_CREATED,
                data = {
                'status': 1, 
                'data': serializer.data
                },
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )        