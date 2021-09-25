
from .models import Policy,Customer
from rest_framework import serializers
from django.conf import settings
from .validators.field_validator import FieldValidator


class PolicyDetailSerializer(serializers.ModelSerializer):
    purchase_date = serializers.DateField(format="%Y-%m-%d", required=False, read_only=True)
    
    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        FieldValidator.validate_premium(data['premium'])
        return data
    
    class Meta:
        model = Policy
        fields = '__all__'
        