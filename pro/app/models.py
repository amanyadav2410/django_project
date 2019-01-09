from django.db import models
from django.core import validators 
class User(models.Model):
	name=models.CharField(max_length=50)
	mobile=models.IntegerField()
	address=models.CharField(max_length=50)
	email=models.EmailField(unique=True)
	cemail=models.EmailField(unique=True)
	def clean(self):
		all_clean_data=super().clean()
		email=all_clean_data['email']
		cemail=all_clean_data['cemail']
		if(email!=cemail):
			raise forms.ValidationError('make sure email match')