from django.db import models

# Create your models here.

class Cinema(models.Model):
    name = models.CharField("Nome", db_index=True, unique=True, max_length=50)
    city = models.CharField("Cidade", max_length=50)
    district = models.CharField("Bairro", max_length=50)
    street = models.CharField("Rua", max_length=50)
    
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    updated = models.DateTimeField(db_index=True, auto_now=True)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = "Cinemas"
        ordering = ['name']