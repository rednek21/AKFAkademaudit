from django.db import models


# Create your models here.
class Contact(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Contact object {self.pk}'
