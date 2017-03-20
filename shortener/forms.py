from django import forms
from .validators import validate_url

class SubmitURLForm(forms.Form):
    url = forms.CharField(label='',
                          max_length=220,
                          validators=[validate_url],
                          widget= forms.TextInput(
                                  attrs={'placeholder':'Long URL',
                                        'class':'form-control'}
                                                  )
                          )
