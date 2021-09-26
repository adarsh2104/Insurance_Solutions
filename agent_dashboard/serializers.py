
from .models import Policy,Customer
from rest_framework import serializers
from django.conf import settings


class PolicyDetailSerializer(serializers.ModelSerializer):
    '''
    Policy Model Serializer for serializing/deserializing Policy objects
    purchase_date : Date Field formatted to "%d-%m-%Y"
    '''
    
    purchase_date = serializers.DateField(format="%d-%m-%Y", required=False, read_only=True)
    
    class Meta:
        model = Policy
        fields = '__all__'
        