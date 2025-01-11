from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

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
    photo            = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    publication      = models.BooleanField(default=False)
    date_publication = models.DateField(default=datetime.now, blank=False)
    user             = models.ForeignKey(
        to=User,
        null=True,
        blank=False,
        related_name="user",
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name
    