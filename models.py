from django.db import models

class Form(models.Model):
    full_name = models.CharField(max_length=80)
    phone = models.CharField(max_length=80)
    national_id = models.CharField(max_length=80)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.full_name}"





