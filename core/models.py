from django.db import models

# Create your models here.
class Instituciones(models.Model):
    id_institucion = models.AutoField(primary_key=True)
    nom_institucion = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom_institucion
    
class Participantes(models.Model):
    ESTADOS_CHOICES = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    ]
    
    id_participante = models.AutoField(primary_key=True)
    nom_participante = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    fecha_inscripcion = models.DateField()
    institucion = models.ForeignKey(Instituciones, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADOS_CHOICES)
    hora_inscripcion = models.TimeField()
    observacion = models.TextField() 
    
    def __str__(self):
        return f"{self.nom_participante} - {self.institucion}"