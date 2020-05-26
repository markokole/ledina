from django.contrib import admin
from .models import Izbira, polja

class IzbiraAdmin(admin.ModelAdmin):

    list_display = ['kandidat'] + polja() + ['created_on']
  
admin.site.register(Izbira, IzbiraAdmin)