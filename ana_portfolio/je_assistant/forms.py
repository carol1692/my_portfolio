from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, label='Search Artist or track', widget=forms.TextInput(attrs={"class": "form-label form-control form_content", "placeholder":"Artist or Track Name", }))