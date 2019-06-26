from django.contrib import admin
from matriculas.models import Perfil, Docente, Estudiante, User, Matricula

# Register your models here.

@admin.register(Perfil)
class Adminperfil(admin.ModelAdmin):
    list_display = ('id','documento','genero','nacimiento','telefono','user',)


@admin.register(Docente)
class Admindocente(admin.ModelAdmin):
    list_display = ('profesion','user',)

@admin.register(Estudiante)
class Adminestudiante(admin.ModelAdmin):
    list_display = ('observador','user',)

@admin.register(Matricula)
class Adminmatricula(admin.ModelAdmin):
    list_display = ('rh', 'estados', 'fecha', 'nombre_estudiante','user',)
    def nombre_estudiante(self,estudianten):
        return "%s" % (estudianten.estudiante.user.first_name)
