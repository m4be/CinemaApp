from django.db import models

# Create your models here.
class Persons(models.Model):


    name = models.CharField('Имя', max_length=50)
    card_number = models.CharField('Номер карты', max_length=19)
    expiry_m = models.CharField('Срок (Месяц)', max_length=2)
    expiry_y = models.CharField('Срок (Год)', max_length=4)
    cvc = models.CharField('CVC код', max_length=3)

    def __str__(self):
        return self.name
