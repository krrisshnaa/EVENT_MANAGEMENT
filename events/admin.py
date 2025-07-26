from django.contrib import admin
from .models import Event, Participant

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location', 'category', 'capacity', 'created_at', 'updated_at')
    search_fields = ('name', 'location')
    list_filter = ('category', 'date')
    ordering = ('date',)

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'event', 'registered_at')
    search_fields = ('name', 'email')
    list_filter = ('event', 'registered_at')
    ordering = ('-registered_at',)