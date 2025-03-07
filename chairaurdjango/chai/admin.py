from django.contrib import admin
from .models import ChaiVariety
from .models import Review

# register you models here
admin.site.register(ChaiVariety)
admin.site.register(Review)
