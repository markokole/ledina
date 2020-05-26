from django import forms
from ledina2.models import Izbira, polja

class IzbiraForm(forms.ModelForm):

    class Meta:
        model = Izbira
        polja = polja()
        fields = polja

    