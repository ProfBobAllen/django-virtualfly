from django.contrib import admin
from .models import Choices

class VflyAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'name')
    ordering = ('symbol',)
    search_fields = ('symbol', 'name')

# Register your models here.
admin.site.register(Choices, VflyAdmin)

