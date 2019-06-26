from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Perfil (models.Model):
    documento=models.CharField(max_length=11)
    genero=((1, "M"),
            (2, "F"),
            (3, "O"),
            )
    genero=models.SmallIntegerField(choices=genero)
    nacimiento=models.DateField()
    telefono=models.CharField(max_length=10)
    user=models.OneToOneField(User, on_delete=models.PROTECT)

    class Meta:
        db_table='perfil'

class Docente(models.Model):
     profesion=models.CharField(max_length=50)
     user=models.OneToOneField(User, on_delete=models.PROTECT)

     class Meta:
         db_table='docente'

class Estudiante(models.Model):
      observador=models.CharField(max_length=100)
      user=models.OneToOneField(User, on_delete=models.PROTECT)

      class Meta:
          db_table='estudiante'

class Matricula(models.Model):
      rh=((1, "O+"),
          (2, "A+"),
          (3, "O-"),
          (4, "AB"),)
      estados=((1, "Activo"),
               (2, "Inactivo"),)
      rh=models.SmallIntegerField(choices=rh)
      fecha=models.DateField()
      estados=models.SmallIntegerField(choices=estados)
      estudiante=models.OneToOneField(Estudiante, on_delete=models.PROTECT)
      user=models.OneToOneField(User, on_delete=models.PROTECT)


      class Meta:
          db_table='matricula'
