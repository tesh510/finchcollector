from django.contrib import admin
from .models import Finch, Feeding
# Register your models here.
admin.site.register(Finch)
# register the new Feeding Model 
admin.site.register(Feeding)