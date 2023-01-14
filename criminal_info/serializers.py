from rest_framework import serializers
from .models import Criminal_Info

class Criminal_InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Criminal_Info
        fields=('__all__')