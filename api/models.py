from distutils.command import upload
import email
import profile
from django.db import models
state_field=((
    ('Bihar','Bihar'),
    ('Jharkhand','Jharkhand'),
    ('UP','UP'),
    ('MP','MP'),
    ('Delhi','Delhi')

)

)
class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    state = models.CharField(choices=state_field, max_length=50)
    gender =models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    profile_img = models.ImageField(upload_to = "pimages",blank=True)
    resume_doc = models.FileField(upload_to='rdocs',blank=True)
    