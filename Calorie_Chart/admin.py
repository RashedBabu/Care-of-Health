from django.contrib import admin
from .models import Veg, Fruits, Carb, Protein, Fat, Others

# Register your models here.
admin.site.register(Veg)
admin.site.register(Fruits)
admin.site.register(Carb)
admin.site.register(Protein)
admin.site.register(Fat)
admin.site.register(Others)