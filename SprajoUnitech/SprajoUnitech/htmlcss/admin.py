from django.contrib import admin
from .models import Sprajo
# Register your models here.
@admin.register(Sprajo)
class SprajoAdmin(admin.ModelAdmin):
    list_display = ('id','Name','Image','description','capacity','unit','price')
