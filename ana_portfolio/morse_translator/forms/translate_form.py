from django import forms

class MorseForm(forms.Form):
    input_text = forms.CharField(label="Message", widget=forms.Textarea(attrs={"class": "form-control"}))