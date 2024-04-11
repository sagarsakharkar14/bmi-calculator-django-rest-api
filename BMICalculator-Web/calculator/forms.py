from django import forms

class BMICalculatorForm(forms.Form):
    name = forms.CharField(max_length=20)
    height = forms.FloatField(label='Height (in cm)')
    weight = forms.FloatField(label='Weight (in kg)')