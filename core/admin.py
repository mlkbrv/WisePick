from django.contrib import admin
from .models import CPU,GPU,RAM,Needs,Phone,BrandsCoefficients

admin.site.register(CPU)
admin.site.register(GPU)
admin.site.register(RAM)
admin.site.register(Needs)
admin.site.register(Phone)
admin.site.register(BrandsCoefficients)