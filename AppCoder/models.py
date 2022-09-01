from django.db import models

# Create your models here.
    
class Familia(models.Model):

    ap         = models.CharField(max_length=50)
    nom_padre  = models.CharField(max_length=50)
    nom_madre  = models.CharField(max_length=50)
    nom_hijo   = models.CharField(max_length=50)
    padres_nac = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.nom_padre

class Miembro(models.Model):
    nom  = models.CharField(max_length=50)
    ap   = models.CharField(max_length=50)
    edad = models.IntegerField()
    nac  = models.CharField(max_length=20)

    def __str__(self):
        return f"Miembro de la familia: {self.nom} {self.ap} {self.edad} {self.nac}"

""" class Madre(models.Model):

    nom  = models.CharField(max_length=50)
    ap   = models.CharField(max_length=50)
    edad = models.IntegerField()
    nac  = models.CharField(max_length=20)

    def __str__(self):
        return "Madre:" +self.nom+", "+self.ap+", "+self.edad+", "+self.nac

class Hijo(models.Model):

    nom  = models.CharField(max_length=50)
    ap   = models.CharField(max_length=50)
    edad = models.IntegerField()
    nac  = models.CharField(max_length=20)

    def __str__(self):
        return "Hijo:" +self.nom+", "+self.ap+", "+self.edad+", "+self.nac """