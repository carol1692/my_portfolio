from django import forms

class ContactPortfolio(forms.Form):
    user_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={ "class":"form-control"}))
    user_mail = forms.EmailField(label="", widget=forms.TextInput(attrs={"class": "form-control"}))
    message = forms.CharField(label="", widget=forms.Textarea(attrs={"class": "form-control"}))