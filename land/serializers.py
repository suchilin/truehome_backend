from rest_framework import serializers
from .models import Land


class LandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        extra_kwargs = {
            "name": {"required": True, "max_length": 50, "error_messages": {
                "required": "El nombre es requerido",
                "max_lengh": "El nombre debe ser maximo 50 caracteres"
            }},
            "address": {"required": True, "max_length": 100, "error_messages": {
                "required": "La direccion es requerida",
                "max_lengh": "La direccion debe ser maximo 100 caracteres"
            }},
            "area": {"required": True, "error_messages": {
                "required": "Los metros cuadrados son requeridos",
            }}
        }
