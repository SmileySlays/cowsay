from django import forms

class CowsayAddForm(forms.Form):
    text = forms.CharField(max_length=150)