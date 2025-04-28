from rest_framework import viewsets
from Inicio.models import TipoUsuario, Comuna, Region, Direccion, Venta, Categoria, TipoProd, Marca, Modelo, Producto, Detalle
from .serializers import TipoUsuarioSerializer, ComunaSerializer, RegionSerializer, DireccionSerializer, VentaSerializer, CategoriaSerializer, TipoProdSerializer, MarcaSerializer, ModeloSerializer, ProductoSerializer, DetalleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import UsuarioSerializer
from Inicio.models import Usuario


class TipoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = TipoUsuario.objects.all()
    serializer_class = TipoUsuarioSerializer

# Vista para manejar usuarios
class UsuarioAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Protegido con autenticación

    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class TipoProdViewSet(viewsets.ModelViewSet):
    queryset = TipoProd.objects.all()
    serializer_class = TipoProdSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class DetalleViewSet(viewsets.ModelViewSet):
    queryset = Detalle.objects.all()
    serializer_class = DetalleSerializer
