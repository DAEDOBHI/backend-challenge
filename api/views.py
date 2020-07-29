from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class Products(APIView):
    def get(self,request):
        
        return Response(status=status.HTTP_200_OK)

    def post(self,request):
        data = request.data
        try:
            print(data)
            return Response(status=status.HTTP_200_OK)
        except    Exception as err:
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
