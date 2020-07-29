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

    def validate(self, data):
        if len(data['name']) < 3 or len(data['name']) > 55:
            raise serializers.ValidationError(
                'Invalid product name')
        if data['value'] < 0 or data['value'] >= 999999.9:
            raise serializers.ValidationError(
                'Invalid value')
        if data['discount_value'] > data['value']:
            raise serializers.ValidationError(
                'Invalid discount value')
        if data['stock'] <= -1:
            raise serializers.ValidationError(
                'Invalid stock value')
        return data
