from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from apps.galeria.rename import rename_photo

class photographs(models.Model):
    option_category = [
        ("Nebulosa", "Nebulosa"),
        ("Estrela", "Estrela"),
        ("Galáxia", "Galáxia"),
        ("Planeta", "Planeta"),
    ]

    name             = models.CharField(max_length=100, null=False, blank=False)
    credit           = models.CharField(max_length=150, null=False, blank=False)
    category         = models.CharField(max_length=100, choices=option_category, default="")
    title            = models.CharField(max_length=100, null=True, blank=True, default="")
    text             = models.TextField(null=False, blank=False)
    photo            = models.ImageField(upload_to=rename_photo, blank=True)
    publication      = models.BooleanField(default=True)
    date_publication = models.DateField(default=datetime.now, blank=False)
    user             = models.ForeignKey(
        to=User,
        null=True,
        blank=False,
        related_name="user",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
    