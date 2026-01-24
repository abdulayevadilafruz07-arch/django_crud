from django.db import models

# Create your models here.


class davlat(models.Model):
    nomi = models.CharField(max_length=100)
    poytaxti= models.CharField(max_length=100)
    maydoni = models.FloatField()
    aholi_soni = models.BigIntegerField()
    tili=models.CharField(max_length=200)
    pul_birligi=models.CharField(max_length=50)
    qitasi = models.CharField(max_length=50)


    def __str__(self):
        return self.nomi
