from django.contrib import admin
from .models import Plant, Photo, Reminder, Location

# Register your models here.
admin.site.register(Plant)
admin.site.register(Photo)
admin.site.register(Reminder)
admin.site.register(Location)