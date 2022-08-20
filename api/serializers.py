from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from api.models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields = '__all__'
        