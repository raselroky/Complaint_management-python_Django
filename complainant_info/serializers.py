from .models import Complainant_Info
from rest_framework import serializers

class Complainant_InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Complainant_Info
        fields=('__all__')