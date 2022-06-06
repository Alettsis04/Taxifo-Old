from django.db import models


class Persona(models.Model):

    listaGenero = (
        ('femenino','Femenino'),
        ('masculino', 'Masculino')
    )

    persona_id = models.AutoField(primary_key = True)
    cedula = models.CharField(max_length = 10, null = False, unique = True)
    apellidos = models.CharField(max_length = 70, null = False)
    nombres = models.CharField(max_length = 70, null = False)
    genero = models.CharField(max_length = 30, choices = listaGenero, default = 'femenino')
    correo = models.EmailField(max_length = 105)
    telefono = models.CharField(max_length = 15)
    celular = models.CharField(max_length = 15, null = False)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        return self.cedula

class Barrio(models.Model):

    barrio_id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100, null = False, unique = True)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        return self.nombre

class Cliente(models.Model):

    cliente_id = models.AutoField(primary_key = True)
    calle1 = models.CharField(max_length = 100, null = True)
    calle2 = models.CharField(max_length = 100, null = True)
    referencia1 = models.CharField(max_length = 150, null = False)
    referencia2 = models.CharField(max_length = 150, null = True)
    barrio = models.ForeignKey(Barrio, on_delete = models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        return self.persona

class Agente(models.Model):

    listaFunciones = (
        ('chofer','Chofer'),
        ('call center', 'Call Center')
    )

    agente_id = models.AutoField(primary_key = True)
    funcion = models.CharField(max_length = 30, choices = listaFunciones, default = 'femenino')
    persona = models.ForeignKey(Persona, on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        return self.persona