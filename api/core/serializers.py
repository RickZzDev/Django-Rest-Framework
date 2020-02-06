from rest_framework import serializers
from .models import Empresas

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = ('id','nome','cnpj','senha')