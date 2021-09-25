from django.conf import settings
from .exceptions import MaxAllowedPremiumExceeded
from django.utils.translation import gettext_lazy as _



class FieldValidator:
    def validate_premium(value):
        max_premium = settings.MAX_PREMIUM
        if int(value) > max_premium:
            raise ValidationError(
                _('%(value) USD is greater than max allowed premium : %(max_premium)'),
                params={'value': value,'max_premium':max_premium},
            )