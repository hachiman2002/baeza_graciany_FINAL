from rest_framework import serializers
from core import models

class ParticipanteSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Participantes
        fields = '__all__'

class InstitucionSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Instituciones
        fields = '__all__'