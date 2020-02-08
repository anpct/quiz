from django.db import models
from django.db.models import Model 
from django.core.exceptions import ValidationError
from django.conf import settings

def validate_roll(roll_no):
    if len(roll_no) == 10:
        return
    else:
        raise ValidationError("INVALID ROLL NO")

def validate_key(key):
    if key in settings.ALLOWED_PASSKEY:
        return
    else:
        raise ValidationError("INVALID PASSKEY NO")


class Resp(Model):

    class Meta:
        unique_together = (('roll_no', 'passkey'),)

    CHOICES =( 
    ("1", "MRIET"), 
    ("2", "OTHERS") ) 
    
    roll_no = models.CharField(max_length = 10, null = False, blank = False, validators=[validate_roll])
    name = models.CharField(max_length = 50, null = False, blank = False)
    passkey = models.CharField(max_length = 6, null = False, blank = False, validators=[validate_key])
    college = models.CharField(max_length = 10, null = False, blank = False, choices = CHOICES)
    resp = models.CharField(max_length = 30, null = True, blank = True)


    def save(self, force_insert=False, force_update=False):
        self.roll_no = self.roll_no.upper()
        super(Resp, self).save(force_insert, force_update)


