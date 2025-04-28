from rest_framework import serializers
from Inicio.models import Usuario, Producto, Marca, Categoria

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'  # Trae todos los campos 

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Producto
        fields= '__all__'

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Marca
        fields= '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'