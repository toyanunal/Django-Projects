from django.db import models
# SuperUserInformation
# User: toyanunal
# Email: toyanunal@gmail.com
# Password: password

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, unique=True)
