from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header="Groziit Dynamic Spaces"
admin.site.register(Jobs)
admin.site.register(Profiles)