from django.contrib import admin
from .models import Plant, Photo, Reminder

# Register your models here.
admin.site.register(Plant)
admin.site.register(Photo)
admin.site.register(Reminder)