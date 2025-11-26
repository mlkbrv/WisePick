from django.contrib import admin
from .models import CPU,GPU,RAM,Needs,Phone,BrandsCoefficients

admin.site.register(CPU)
admin.site.register(GPU)
admin.site.register(RAM)
admin.site.register(Needs)
admin.site.register(BrandsCoefficients)

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'year', 'ram_size', 'memory_size')
    list_filter = ('brand', 'year', 'os_type')
    search_fields = ('name', 'brand__name', 'processor')