from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class korisnici(AbstractUser):
    id = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=50)
    status = models.CharField(max_length=50)



class predmeti(models.Model):
    id = models.IntegerField(primary_key=True)
    ime = models.CharField(max_length=255)
    kod = models.CharField(max_length=16)
    program = models.TextField()
    bodovi = models.IntegerField()
    sem_redovni = models.IntegerField()
    sem_izvanredni = models.IntegerField()
    izbori = (('da','Da'),('ne','Ne'))

class upisi(models.Model):
    student_id = models.ForeignKey(korisnici, on_delete=models.CASCADE)
    predmet_id = models.ForeignKey(predmeti, on_delete=models.CASCADE)
    lastname = models.CharField(max_length=64)
