from django.db import models

from cinemas.models import Cinema

# Create your models here.

class Room(models.Model):
    name = models.CharField("Identificação da sala")
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.cinema} - {self.name}"
    
class Seat(models.Model):
    SEAT_TYPES = (
        ('df', 'Default'),
        ('hc', 'Handicapped'),
        ('db', 'D-Box'),
        ('bk', 'Blocked'),
        ('vp', 'VIP')
    )
    
    row = models.CharField("Identificador da linha da poltrona", max_length=1)
    column = models.SmallIntegerField("Número da poltrona")
    type = models.CharField("Tipo da poltrona", choices=SEAT_TYPES, max_length=2)
    