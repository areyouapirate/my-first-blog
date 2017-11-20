from django.contrib import admin
from .models import Post, Inscription
from mapwidgets.widgets import GooglePointFieldWidget
from django.contrib.gis.db import models
from django.contrib.gis import admin as gis_admin

admin.site.register(Post)
admin.site.register(Inscription)


class PlaceAdmin(gis_admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }
