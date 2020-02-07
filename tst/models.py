from django.db import models
from django.db.models import Model 
from django.core.exceptions import ValidationError

def validate_roll(roll_no):
    if len(roll_no) == 10 and "w91a0" in roll_no.lower():
        return
    else:
        raise ValidationError("INVALID ROLL NO")

def validate_key(key):
    if len(key) == 6 and key in ['ta2n2j', 'a2vceu', 'n26qxl']:
        return
    else:
        raise ValidationError("INVALID PASSKEY NO")


class Resp(Model):

    class Meta:
        unique_together = (('roll_no', 'passkey'),)
    
    roll_no = models.CharField(max_length = 10, null = False, blank = False, validators=[validate_roll])
    name = models.CharField(max_length = 50, null = False, blank = False)
    passkey = models.CharField(max_length = 6, null = False, blank = False, validators=[validate_key])
    resp = models.CharField(max_length = 30, null = True, blank = True)



