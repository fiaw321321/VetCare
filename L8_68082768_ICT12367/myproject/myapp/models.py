from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='ชื่อประชากร')
    age = models.IntegerField(verbose_name='อายุ')

    def __str__(self):
        return self.name
