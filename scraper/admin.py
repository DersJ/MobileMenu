from django.contrib import admin
from scraper import models

# Register your models here.
@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    pass

