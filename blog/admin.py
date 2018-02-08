from django.contrib import admin
from .models import Post, Inscription, Place
from mapwidgets.widgets import GooglePointFieldWidget
from django.contrib.gis.db import models
from django.contrib.gis import admin as gis_admin



class PlaceAdmin(gis_admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }
class PostAdmin(admin.ModelAdmin):
	fields = ('title', 'subtitle', 'text', 'img', 'image_tag', )
	readonly_fields = ('image_tag',)

        

admin.site.register(Post, PostAdmin)
admin.site.register(Inscription)
admin.site.register(Place, PlaceAdmin)