from django.urls import path
from .views import Index, InstitucionCreateView, ParticipanteCreateView, ParticipanteList_class, Participante_detalle_class
from core import views

core_patterns = ([
    path('', Index.as_view(), name='index'),
    #Formulario
    path('formularioInstitucion/', InstitucionCreateView.as_view(), name='formulario-institucion'),
    path('formularioParticipante/', ParticipanteCreateView.as_view(), name='formulario-participante'),
    #autor (Json)
    path('autorJson/', views.autor, name='autor'),
    #Participantes (Class Based Views)
    path('participanteListClass/', ParticipanteList_class.as_view(), name='participanteListClass'),
    path('participanteDetalleClass/<int:id>/', Participante_detalle_class.as_view(), name='estudiantDetalleClass'),
    #Institucion (Función Based Views)
    path('institucionList/', views.institucion_list, name='institucionList'),
    path('institucionDetalle/<int:id>/', views.institucion_detalle, name='institucionDetalle'),
],'core')