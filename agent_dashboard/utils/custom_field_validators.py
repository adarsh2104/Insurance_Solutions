from django.core.exceptions import ValidationError
from django.conf import settings


def premium_field_validator(value):
    '''
    Custom validator for Premium field of Policy Model
    
    for improved error reporting and validation grouping.
        - Validate Premium against allowed : Max Value , Min Value 
    '''
    params = {'show_value': value, 'value': value}
    
    # Validate premium value against max allowed premium.
    if value > settings.MAX_ALLOWED_PREMIUM:
        params['limit_value'] = settings.MAX_ALLOWED_PREMIUM
        message = 'Entered value is greater than Max Allowed \n-Max Allowed Premium  = %(limit_value)s USD \n-Entered Premium\
            = %(show_value)s USD'        
    
    # Validate premium value against min allowed premium.
    elif value < 0:
        params['limit_value'] = 0
        message = 'Entered value is less than Min Allowed  \n-Min Allowed Premium   = %(limit_value)s USD \n-Entered Premium\
            = %(show_value)s USD'
    else:
        return value
    raise ValidationError(message,code=None, params=params)


