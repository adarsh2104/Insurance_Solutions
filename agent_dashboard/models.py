from django.db import models
# from .validators.field_validator import FieldValidator
from django.conf import settings
from django.core.validators import MaxValueValidator,MinValueValidator
# from agent_dashboard.models import Customer,Policy

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name  = models.CharField(max_length=255,null=True)
    last_name   = models.CharField(max_length=255,null=True)

    class Meta:
        # managed = False
        db_table = 'customer'


class Policy(models.Model):
    '''
    For saving search keywords and for giving search sugguestions
    '''
    policy_id = models.AutoField(primary_key=True)
    fk_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    purchase_date = models.DateField(auto_now_add=True)
    premium = models.DecimalField(max_digits=10,decimal_places=2,validators=[MaxValueValidator(settings.MAX_PREMIUM),MinValueValidator(0)])
    region  = models.CharField(max_length=50,null=True)


    class Meta:
        # managed = False
        db_table = 'policy'
        indexes = [
            models.Index(fields=['fk_customer_id']),
        ]


