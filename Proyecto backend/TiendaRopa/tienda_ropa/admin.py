from django.contrib import admin
from django import forms
from .models import Coleccion, Elemento, TerminosLegales

class ElementoForm(forms.ModelForm):
    class Meta:
        model = Elemento
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ElementoForm, self).__init__(*args, **kwargs)
        self.fields['coleccion'].widget = forms.widgets.Select(choices=Coleccion.objects.values_list('id', 'nombre'))

class ElementoInline(admin.TabularInline):
    model = Elemento
    form = ElementoForm

class TerminosLegalesAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo')
    search_fields = ['titulo']

class ColeccionAdmin(admin.ModelAdmin):
    inlines = [ElementoInline]
    list_display = ('nombre', 'fecha_creacion')
    search_fields = ['nombre']

class ElementoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'coleccion_nombre', 'cantidad', 'genero', 'precio', 'tallas', 'imagen', 'imagen_dos', 'imagen_tres')
    list_filter = ('coleccion__nombre', )

    def coleccion_nombre(self, instance):
        return instance.coleccion.nombre
    coleccion_nombre.short_description = 'Colección'

admin.site.register(Coleccion, ColeccionAdmin)
admin.site.register(Elemento, ElementoAdmin)
admin.site.register(TerminosLegales, TerminosLegalesAdmin)