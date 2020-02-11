from django.db.models import Model
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


def validate_key(key):
    if key in settings.ALLOWED_PASSKEY:
        return
    else:
        raise ValidationError("INVALID PASSKEY NO")


# Create your models here.
class Resp(Model):
    
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
    passkey = models.CharField(max_length = 6, null = False, blank = False, validators=[validate_key])
    resp = models.CharField(max_length = 30, null = True, blank = True)