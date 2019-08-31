from django.contrib import admin

from . models import Ad

class AdsAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Ad, AdsAdmin)
