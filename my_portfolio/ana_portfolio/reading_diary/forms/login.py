from django import forms
from django.core.validators import MaxLengthValidator, MinLengthValidator, EmailValidator

class NewUser(forms.Form):
    user_name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={ "class":"field_input"} ))
    user_email = forms.EmailField(label='E-mail', required=True, validators=[EmailValidator(message="Invalid Email")], widget=forms.TextInput(attrs={ "class":"field_input"} ))
    user_password = forms.CharField(label='Password', validators=[MinLengthValidator(8, 'Password should have minimun of 8 characters'), MaxLengthValidator(100, 'Maximun lenght of password is 100 characters')], widget=forms.TextInput(attrs={ "class":"field_input"} ))
    repeat_password = forms.CharField(label='Repeat password', validators=[MinLengthValidator(8, 'Password should have minimun of 8 characters'), MaxLengthValidator(100, 'Maximun lenght of password is 100 characters')], widget=forms.TextInput(attrs={ "class":"field_input"} ))
