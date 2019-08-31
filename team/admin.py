from django.contrib import admin

from .models import Team, Seniority

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class SeniorityAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(Team, TeamAdmin)
admin.site.register(Seniority, SeniorityAdmin)

