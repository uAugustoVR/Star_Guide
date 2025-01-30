from django.contrib import admin
from apps.galeria.models import photographs

class ListPhotograpy(admin.ModelAdmin):
    list_display = ("id", "name", "credit", "date_publication", "publication")
    list_display_links = ("id", "name")
    search_fields = ("name", "category")
    list_filter = ("category", "user")
    list_editable = ("publication",)
    list_per_page = 10

admin.site.register(photographs, ListPhotograpy)