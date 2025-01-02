from django.db import models
import uuid

GENERO_CHOICES = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('U', 'Unisex'),
    ]

class Coleccion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(max_length=1000, null=True, blank=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to='collecciones/', null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'tienda_ropa'

    
class Elemento(models.Model):

    id_elemento = models.UUIDField(primary_key=True,
        default=uuid.uuid4, editable=False)
    coleccion = models.ForeignKey(Coleccion, related_name='elementos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    genero = models.CharField(max_length=50, choices=GENERO_CHOICES)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tallas = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='elementos/')
    imagen_dos = models.ImageField(upload_to='elementos/', null=True, blank=True)
    imagen_tres = models.ImageField(upload_to='elementos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'tienda_ropa'

class TerminosLegales(models.Model):
    titulo = models.CharField(max_length=255, null=True, blank=True)
    subtitulo = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Términos Legales"