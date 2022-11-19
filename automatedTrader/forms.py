from django import forms

# creating a form: 
class InputForm(forms.Form):
    exchange = forms.CharField(label='Exchange', initial='For quick testing, type N')
    exchangeType = forms.CharField(label='Exchange Type', initial='For quick testing, type C')
    scripCode = forms.CharField(initial='For quick testing, type 1660', label='Scrip Code')
    # CHOICES = [('1', '1m'),('2', '5m')]
    # timeframe = forms.ChoiceField(choices=CHOICES, widget=forms.Select())
    # startdate= forms.DateField()
    # enddate= forms.DateField()

from .models import GeeksModel
 
# create a ModelForm
class GeeksForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = GeeksModel
        fields = "__all__"


    
    


