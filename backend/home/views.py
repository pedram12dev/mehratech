from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from .models import Home
from .serializers import HomePageSerializer
from employees.models import Employee
from employees.serializers import EmployeeSerializer


class HomePageView(APIView):
    """
    API view to handle Home page data.
    """

    def get(self, request):
        """
        Retrieve the home page data.
        """
        home = Home.objects.all()
        employee = Employee.objects.all()
        if home:
            serializer = HomePageSerializer(home,many=True, context={'request': request})
            employee_serializer = EmployeeSerializer(employee, many=True, context={'request': request})
            return Response({"home": serializer.data, "employees": employee_serializer.data}, status=status.HTTP_200_OK)
        return Response({"detail": "Home page not found."}, status=status.HTTP_404_NOT_FOUND)
