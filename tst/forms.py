from django import forms
from tst.models import Resp

class RegForm(forms.ModelForm):
    class Meta:
        model = Resp
        fields = ['roll_no', 'name', 'college', 'passkey']
