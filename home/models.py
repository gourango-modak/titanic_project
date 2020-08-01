from django.db import models

# Create your models here.
class TitanicData(models.Model):
    name                = models.CharField(max_length=200)
    sex                 = models.CharField(max_length=20)
    ticket_no           = models.CharField(max_length=100, blank=True, null=True)
    age                 = models.IntegerField(default=0)
    siblings            = models.IntegerField(default=0)
    pclass              = models.IntegerField(default=0)
    cabin_no            = models.CharField(max_length=100, blank=True, null=True)
    fare                = models.IntegerField(default=0)
    embarked            = models.CharField(max_length=1)
    parch               = models.IntegerField(default=0)
    survived            = models.IntegerField(default=0)