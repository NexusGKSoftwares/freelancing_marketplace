from django.contrib import admin
from .models import SystemHealth

@admin.register(SystemHealth)
class SystemHealthAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'cpu_usage', 'memory_usage', 'disk_space')
    list_filter = ('timestamp',)
    search_fields = ('timestamp',)
