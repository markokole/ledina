from django.db import models
from django.contrib.auth.models import User

JEZIK = (
    (0, 'IZBERI'),
    (1, 'NEMŠČINA'),
    (2, 'FRANCOŠČINA'),
    (3, 'ŠPANŠČINA'),
    (4, 'ITALIJANŠČINA'),
    (5, 'RUŠČINA'),
    (6, 'NEMŠČINA N')
)

TOCKE = [(i,i) for i in range(145, 176)]

SPOL = (
    (0, "Ni podatka"),
    (1, "Moski"),
    (2, "Zenski"),
)

POLJA = ['tocke', 'jezik1', 'jezik2', 'jezik3', 'jezik4', 'jezik5', 'jezik6']

class Kandidat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    spol = models.IntegerField(choices=SPOL, default=0, verbose_name="Spol")

class Izbira(models.Model):
    id = models.AutoField(primary_key=True)
    kandidat = models.ForeignKey(User, on_delete=models.CASCADE)
    tocke = models.IntegerField(choices=TOCKE, verbose_name="Seštevek točk ocen")
    jezik1 = models.IntegerField(choices=JEZIK, default=0, verbose_name="Prva želja")
    jezik2 = models.IntegerField(choices=JEZIK, default=0, verbose_name="Druga želja")
    jezik3 = models.IntegerField(choices=JEZIK, default=0, verbose_name="Tretja želja")
    jezik4 = models.IntegerField(choices=JEZIK, default=0, verbose_name="Četrta želja")
    jezik5 = models.IntegerField(choices=JEZIK, default=0, verbose_name="Peta želja")
    jezik6 = models.IntegerField(choices=JEZIK, default=0, verbose_name="Šesta želja")
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.kandidat)

def jezik():
    return dict(JEZIK)

def polja():
    return POLJA