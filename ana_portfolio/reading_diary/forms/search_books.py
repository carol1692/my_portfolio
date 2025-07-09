from django import forms

class SearchBooks(forms.Form):
    search_book = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ "class":"field_input"} ))