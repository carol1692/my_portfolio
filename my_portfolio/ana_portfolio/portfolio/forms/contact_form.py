from django import forms

class ContactPortfolio(forms.Form):
    user_name = forms.CharField(label="Name", max_length=100, widget=forms.TextInput(attrs={ "class":"form-control"}))
    user_mail = forms.EmailField(label="E-mail", widget=forms.TextInput(attrs={"class": "form-control"}))
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={"class": "form-control"}))