from django.db import models

class photographs(models.Model):
    option_category = [
        ("Nebulosa", "Nebulosa"),
        ("Estrela", "Estrela"),
        ("Galáxia", "Galáxia"),
        ("Planeta", "Planeta"),
    ]

    name        = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=150, null=False, blank=False)
    category    = models.CharField(max_length=100, choices=option_category, default='')
    title       = models.CharField(max_length=100, null=True, blank=True, default=" ")
    text        = models.TextField(null=False, blank=False)
    photo       = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"photographs [name={self.name}]"
    