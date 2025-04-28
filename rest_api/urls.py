from django.urls import path, include
from rest_framework import routers
from .views import TipoUsuarioViewSet, ComunaViewSet, RegionViewSet, DireccionViewSet, VentaViewSet, CategoriaViewSet, TipoProdViewSet, MarcaViewSet, ModeloViewSet, ProductoViewSet, DetalleViewSet
from rest_api.views import UsuarioAPIView

router = routers.DefaultRouter()
router.register(r'tipousuarios', TipoUsuarioViewSet)
router.register(r'comunas', ComunaViewSet)
router.register(r'regiones', RegionViewSet)
router.register(r'direcciones', DireccionViewSet)
router.register(r'ventas', VentaViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'tipoproductos', TipoProdViewSet)
router.register(r'marcas', MarcaViewSet)
router.register(r'modelos', ModeloViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'detalles', DetalleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('usuarios/', UsuarioAPIView.as_view(), name="usuarios"),
]
