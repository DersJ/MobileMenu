from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from phonenumber_field.formfields import PhoneNumberField
from scraper.models import *
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
	
	name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Inform a valid email address.')
	phone = PhoneNumberField(label="Phone Number", help_text='We will never share your phone number with anyone.')
	

	class Meta:
		model = get_user_model()
		fields = ('username', 'name', 'email', 'phone', 'password1', 'password2', )


class UpdateProfileForm(ModelForm):
	email = forms.EmailField(max_length=254, help_text='Inform a valid email address.')
	phone = PhoneNumberField(label="Phone Number", help_text='We will never share your phone number with anyone.')
	locations = forms.ModelMultipleChoiceField(queryset=Location.objects.all())
	class Meta:
		model = get_user_model()
		fields = ('email', 'phone', 'locations', 'meals')
	
	def __init__(self, *args, **kwargs):
		super(UpdateProfileForm, self).__init__(*args, **kwargs)
		self.fields["locations"].widget = forms.widgets.CheckboxSelectMultiple()