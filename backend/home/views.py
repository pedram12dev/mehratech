from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from .models import Home
from .serializers import HomePageSerializer


class HomePageView(APIView):
    """
    API view to handle Home page data.
    """

    def get(self, request):
        """
        Retrieve the home page data.
        """
        home = Home.objects.all()
        if home:
            serializer = HomePageSerializer(home,many=True, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "Home page not found."}, status=status.HTTP_404_NOT_FOUND)
