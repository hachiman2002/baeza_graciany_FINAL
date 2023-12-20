from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .models import Instituciones, Participantes
from .forms import FormularioInstitucion, FormularioParticipante

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from django.http import JsonResponse

from rest_framework.decorators import api_view

from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response

from .serializers import ParticipanteSerializers, InstitucionSerializers

# Create your views here.
class Index(TemplateView):
    template_name = "core/index.html"

#Formularios
class InstitucionCreateView(CreateView):
    model = Instituciones
    form_class = FormularioInstitucion
    success_url = reverse_lazy('core:index')

class ParticipanteCreateView(CreateView):
    model = Participantes
    form_class = FormularioParticipante
    success_url = reverse_lazy('core:index')
    
    def form_valid(self, form):
        # Obtener el nombre de la institución desde el formulario
        institucion_nombre = form.cleaned_data['institucion']
        # Guardar la institución si no existe
        institucion, created = Instituciones.objects.get_or_create(nom_institucion=institucion_nombre)
        # Asignar la institución al participante antes de guardar
        form.instance.institucion = institucion
        # Llamar al método form_valid de la clase padre para continuar con el proceso de guardado
        return super().form_valid(form)
    
# Datos Autor proyecto (Json)
def autor(request):
    aut = {
        'id' : 1010,
        'nombre': 'Graciany',
        'apellidoPaterno' : 'Baeza',
        'apellidoMaterno' : 'Jara',
        'correo': 'graciany.baeza@inacapmail.cl',
        'repositorio': 'https://github.com/hachiman2002/baeza_graciany_FINAL',
        'descripcion': 'Prueba 3 y 4 ramo backend, Django Rest Framework'
    }
    return JsonResponse(aut)

#Participantes (Class Based Views)
class ParticipanteList_class(APIView):
    def get(self, request):
        parti = Participantes.objects.all()
        serial = ParticipanteSerializers(parti, many=True)
        return Response(serial.data)
    
    def post(self, request):
        serial = ParticipanteSerializers(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Participante_detalle_class(APIView):
    def get_object(self, id):
        try:
            return Participantes.objects.get(pk=id)
        except Participantes.DoesNotExist:
            return Http404
    
    def get(self, request, id):
        parti = self.get_object(id)
        serial = ParticipanteSerializers(parti)
        return Response(serial.data)
    
    def put(self, request, id):
        parti = self.get_object(id)
        serial = ParticipanteSerializers(parti, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        estude = self.get_object(id)
        estude.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#Institucion (Función Based Views)
@api_view(['GET', 'POST'])
def institucion_list(request):
    if request.method == 'GET':
        insti = Instituciones.objects.all()
        seria = InstitucionSerializers(insti, many=True)
        return Response(seria.data)
    
    if request.method == 'POST':
        seria = InstitucionSerializers (data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status=status.HTTP_201_CREATED)
        return Response(seria.data, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def institucion_detalle(request, id):
    try:
        insti = Instituciones.objects.get(pk=id)
    except Instituciones.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serial = InstitucionSerializers(insti)
        return Response(serial.data)
    
    if request.method == "PUT":
        serial = InstitucionSerializers(insti, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        insti.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)