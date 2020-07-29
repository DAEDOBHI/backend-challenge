from rest_framework import serializers

from api.models import Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id',
                  'name',
                  'value',
                  'discount_value',
                  'stock']
