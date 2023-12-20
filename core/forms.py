from django import forms
from .models import Instituciones, Participantes

class FormularioInstitucion(forms.ModelForm):
    nom_institucion = forms.CharField(widget=forms.DateInput(attrs={'class': 'form-control'}), label='Nombre institucion')
    class Meta:
        model = Instituciones
        fields = '__all__'

class FormularioParticipante(forms.ModelForm):
    nom_participante = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Nombre Participante')
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Telefono')
    fecha_inscripcion = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}), label='Fecha de inscripcion (YYYY-MM-DD)')
    hora_inscripcion = forms.TimeField(widget=forms.DateInput(attrs={'class': 'form-control'}), label='Hora Inscripcion (HH:MM)')
    observacion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Observacion')
    class Meta:
        model = Participantes
        fields = ['nom_participante', 'telefono', 'fecha_inscripcion', 'institucion', 'estado', 'hora_inscripcion', 'observacion']

    def __init__(self, *args, **kwargs):
        super(FormularioParticipante, self).__init__(*args, **kwargs)
        self.fields['institucion'].queryset = Instituciones.objects.all()
        self.fields['institucion'].label_from_instance = lambda obj: obj.nom_institucion