from django.contrib import admin

# Register your models here.
from isobres.models import Donor, Sobre

admin.site.register(Sobre)
admin.site.register(Donor)
