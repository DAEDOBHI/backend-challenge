from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Products
from .serializers import ProductSerializer


class ProductsApiView(APIView):
    def get(self, request):
        queryset = Products.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
