from rest_framework import serializers
from .models import BMIRecord

class BMIRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BMIRecord
        fields = ('id', 'weight', 'height', 'created_at')
