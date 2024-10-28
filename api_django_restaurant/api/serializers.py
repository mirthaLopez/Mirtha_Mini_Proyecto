from rest_framework import serializers
from .models import Cliente, Categoria, Menu, Orden, DetalleOrden

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_nombre(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El nombre debe tener más de 2 letras.")
        return value

    def validate_email(self, value):
        if '@' not in value:
            raise serializers.ValidationError("El correo electrónico debe contener el símbolo '@'.")
        return value

    def validate_contraseña(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        return value

    def validate_rol(self, value):
        if value not in ['cliente', 'administrador']:
            raise serializers.ValidationError("El rol debe ser 'cliente' o 'administrador'.")
        return value

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

    def validate_nombre(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El nombre de la categoría debe tener más de 2 letras.")
        return value

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

    def validate_nombre(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El nombre del menú debe tener más de 2 letras.")
        return value

    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio debe ser un valor positivo.")
        return value

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'

    def validate_estado(self, value):
        if value not in ['preparación', 'enviado', 'entregado']:
            raise serializers.ValidationError("El estado debe ser uno de los siguientes: preparación, enviado, entregado.")
        return value

class DetalleOrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleOrden
        fields = '__all__'

    def validate_cantidad(self, value):
        if value <= 0:
            raise serializers.ValidationError("La cantidad debe ser un valor positivo.")
        return value

    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio debe ser un valor positivo.")
        return value
