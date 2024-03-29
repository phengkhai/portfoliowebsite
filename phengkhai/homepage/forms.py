from django import forms

# Create your forms here.

class ContactForm(forms.Form):
	organization_name = forms.CharField(max_length = 50)
	position_name = forms.CharField(max_length = 50)
	email = forms.CharField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)