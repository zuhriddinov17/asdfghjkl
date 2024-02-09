from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    job = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def str(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)

    def str(self):
        return self.name