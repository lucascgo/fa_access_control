from django.db import models

class Code(models.Model):
    qrcode = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.qrcode
