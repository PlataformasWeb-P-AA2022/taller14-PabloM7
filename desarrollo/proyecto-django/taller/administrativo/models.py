from django.db import models

# Create your models here.

class Propietario(models.Model):
    opciones_nacionalidad = (
        ('ecuatoriana','Ecuatoriana'),
        ('peruana','Peruana'),
        ('colombiana','Colombiana')
    )

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.CharField(max_length=30, unique=True)
    nacionalidad = models.CharField(max_length=30,
                                    choices=opciones_nacionalidad)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.apellido,
                self.edad,
                self.nacionalidad)

class Departamento(models.Model):
    costo = models.CharField(max_length=100)
    ncuartos = models.CharField(max_length=100)
    nbaños = models.CharField(max_length=100)
    valicuota = models.CharField(max_length=100)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE,
            related_name="propietario")

    def __str__(self):
        return "%s %s %s %s" % (self.costo,
                self.ncuartos,
                self.nbaños,
                self.valicuota)