from django.contrib import admin
from galeria.models import Fotografia

# Register your models here.
class ListandoFotografias(admin.ModelAdmin):
	list_display = ("id", "name", "legenda", "publicado")
	list_display_links = ("id", "name")
	search_fields = ("name", )
	list_filter = ("categoria", )
	list_per_page = 10
	list_editable = ("publicado", )

admin.site.register(Fotografia, ListandoFotografias)