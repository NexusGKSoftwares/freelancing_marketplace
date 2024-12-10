from django.contrib import admin
from .models import SystemSetting, StaticPage

class StaticPageInline(admin.TabularInline):
    model = StaticPage
    fields = ('page', 'title', 'content')
    extra = 0  # Do not show extra empty rows
    max_num = len(StaticPage.PAGE_CHOICES)  # Limit to predefined pages
    can_delete = False  # Prevent deleting pages from admin

@admin.register(SystemSetting)
class SystemSettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_at')
    search_fields = ('name',)
    inlines = [StaticPageInline]

