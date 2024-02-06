from django.db import models

# Create your models here.
class Employee(models.Model):

    eNo = models.IntegerField()
    eName = models.CharField(max_length = 50)
    eSal = models.FloatField()
    eAdd = models.CharField(max_length = 100)
    eMarks = models.IntegerField(default = 0)

    # def __str__(self):
    #     return self.eName
