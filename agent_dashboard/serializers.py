
from .models import Policy,Customer
from rest_framework import serializers
from django.conf import settings
# from .validators.field_validator import FieldValidator


class PolicyDetailSerializer(serializers.ModelSerializer):
    purchase_date = serializers.DateField(format="%d-%m-%Y", required=False, read_only=True)
    
    class Meta:
        model = Policy
        fields = '__all__'
        