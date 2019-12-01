from rest_framework import serializers
from .models import Land
import re


class LandSerializer(serializers.ModelSerializer):
    squaremeters = serializers.IntegerField(default='', required=False)

    def validate_squaremeters(self, value):
        try:
            int(value)
        except:
            raise serializers.ValidationError('Introduce un numero valido')
        if(value < 0):
            raise serializers.ValidationError(
                'Introduce un valor entero positivo')
        if(value > 99999):
            raise serializers.ValidationError(
                'Debe ser un valor de 5 digitos o menos')
        return value

    class Meta:
        model = Land
        fields = ['name', 'address', 'squaremeters', 'email']
        extra_kwargs = {
            'name': {
                'required': True,
                'max_length': 50,
                'error_messages': {
                    'required': 'El nombre es requerido',
                    'blank': 'El nombre es requerido',
                    'max_length': 'El nombre debe ser hasta 50 caracteres'
                }
            },
            'address': {
                'required': True,
                'max_length': 100,
                'error_messages': {
                    'required': 'La direccion es requerida',
                    'blank': 'La direccion es requerida',
                    'max_legth': 'La direccion debe ser hasta 100 caracteres'
                }
            },
            'email': {
                'required': True,
                'max_length': 50,
                'error_messages': {
                    'required': 'El email es requerido',
                    'blank': 'El email es requerido',
                    'invalid': 'Email invalido',
                    'max_length': 'El email debe ser hasta 50 caracteres'
                }
            }
        }
