from django.db import models
from django.conf import settings
from agent_dashboard.utils.custom_field_validators import premium_field_validator


class Customer(models.Model):
    '''
    Model for saving Customer details
    primary key : customer_id
    '''
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'customer'


class Policy(models.Model):
    '''
    Model for storing purachased policy by the client
    
    Primary key : policy_id   
    Index : fk_customer to optimize searching by customer_id
    premium_field_validator : Custom validator to validate  premium value against allowd min and max values 
    '''
    
    policy_id = models.AutoField(primary_key=True)
    fk_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    purchase_date = models.DateField(auto_now_add=True)
    region = models.CharField(max_length=50, null=True)
    premium = models.DecimalField(max_digits=10, decimal_places=2, validators=[premium_field_validator])

    class Meta:
        db_table = 'policy'
        indexes = [
            models.Index(fields=['fk_customer_id']),
        ]
