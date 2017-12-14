from django.contrib import admin
from .models import Post, Inscription, Place
from mapwidgets.widgets import GooglePointFieldWidget
from django.contrib.gis.db import models
from django.contrib.gis import admin as gis_admin



class PlaceAdmin(gis_admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }


admin.site.register(Post)
admin.site.register(Inscription)
admin.site.register(Place, PlaceAdmin)