from django.db import models



def validate_key(key):
    if key in settings.ALLOWED_PASSKEY:
        return
    else:
        raise ValidationError("INVALID PASSKEY NO")


# Create your models here.
class Resp(models.Model):
    
    class Meta:
        unique_together = (('roll_no', 'passkey'),)
    
    roll_no = models.models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=_(""))
    passkey = models.CharField(max_length = 6, null = False, blank = False, validators=[validate_key])
    resp = models.CharField(max_length = 30, null = True, blank = True)