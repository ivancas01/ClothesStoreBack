from rest_framework.routers import DefaultRouter
from .views import ColeccionViewSet, ElementoViewSet, TerminosLegalesViewSet

router = DefaultRouter()
router.register(r'colecciones', ColeccionViewSet, basename='coleccion')
router.register(r'elementos', ElementoViewSet, basename='elemento')
router.register(r'terminos', TerminosLegalesViewSet, basename='terminos')

urlpatterns = router.urls