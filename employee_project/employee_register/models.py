from django.db import models
import uuid

class Employee(models.Model):

    objects = models.Manager()
    name=models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.name
