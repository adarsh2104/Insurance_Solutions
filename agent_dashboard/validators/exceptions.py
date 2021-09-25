from django.core.exceptions import ValidationError


class MaxAllowedPremiumExceeded(ValidationError):
    '''Exception raised when video content is compared with image content'''
    pass
    # def __str__(self):
    #     return 'Cannot compare video content with image content'
