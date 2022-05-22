from email.policy import default
from django.db import models

# Create your models here.
class users(models.Model):
    fastid=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=200)
    vehnum=models.CharField(max_length=200)
    fine=models.IntegerField(default=0)
    accbal=models.IntegerField(default=0)

    def __str__(self):
        return self.username


