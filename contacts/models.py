from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Phone(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.phone