from django.db import models

# Create your models here. 
class Alumno(models.Model):
    nombres=models.CharField(max_length=40)
    apellidos=models.CharField(max_length=40)
    codigo=models.CharField(max_length=10)   
    dni=models.CharField(max_length=8)
    direccion=models.CharField(max_length=80)
    email=models.EmailField()
    telefono=models.CharField(max_length=9)
    facultad=models.CharField(default="INGENIERIA",max_length=10)
    escuela=models.CharField(default="INGENIERIA DE SISTEMAS",max_length=22)
    firma=models.ImageField(upload_to="alumno",null = True)
    estado=models.BooleanField()
    def __str__(self):
        return self.nombres

class TipoTramite(models.Model):
    tipoTramite=models.CharField(max_length=90)
    estado=models.BooleanField()
    def __str__(self):
        return self.tipoTramite

class TipoRequisito(models.Model):
    tipoRequisito=models.CharField(max_length=100)
    tipoTramites=models.ForeignKey(TipoTramite,on_delete=models.CASCADE, null = True)
    estado=models.BooleanField()
    def __str__(self):
        return self.tipoRequisito
    
class Requisito(models.Model):
    requisito=models.CharField(max_length=200)
    archivo=models.FileField(upload_to="requisito",blank = True, null = True) #no es obligatorio (por el tema del fut que no es para todos los trámites)
    tipoRequisitos=models.ForeignKey(TipoRequisito,on_delete=models.CASCADE, null = True)
    estado=models.BooleanField()
    def __str__(self):
        return self.requisito

class Tramite(models.Model):
    tipoTramite=models.ForeignKey(TipoTramite,on_delete=models.CASCADE)
    alumnos=models.ForeignKey(Alumno,on_delete=models.CASCADE, null = True )
    estado=models.BooleanField(default=True)
    
class EstadoTramite(models.Model):
    estadotram=models.CharField(max_length=20) #este es el estado del trámite
    estado=models.BooleanField(default=True) #este es el estado para ver o no ver el trámite
    def __str__(self):
        return self.estadotram

class BandejaTramite(models.Model):
    tramites=models.ForeignKey(Tramite,on_delete=models.CASCADE)
    estadotramites=models.ForeignKey(EstadoTramite,on_delete=models.CASCADE)
    observacion=models.CharField(max_length=200)
    tiempo=models.IntegerField()
    fecha=models.DateTimeField()
    estado=models.BooleanField(default=True)
    def __str__(self):
        return self.observacion
