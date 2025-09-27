from django.contrib import admin
from .models import Alert, Report
from django.utils.html import format_html

# -------------------------------
# Alert Admin (no is_official)
# -------------------------------
class AlertAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')  # show only existing fields
    list_filter = ('date_created',)           # filter only existing fields
    search_fields = ('title', 'description')
    ordering = ('-date_created',)
    readonly_fields = ('date_created',)

# -------------------------------
# Report Admin
# -------------------------------
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'reporter', 'location', 'status', 'date_reported')
    list_filter = ('status', 'date_reported')
    search_fields = ('title', 'description', 'reporter__username')
    ordering = ('-date_reported',)
    readonly_fields = ('date_reported',)

    def colored_status(self, obj):
        color = 'green' if obj.status == 'Approved' else 'orange'
        return format_html('<span style="color:{}; font-weight:bold;">{}</span>', color, obj.status)
    colored_status.short_description = 'Status'
    # Show combined location as "latitude, longitude"
    def location(self, obj):
        return f"{obj.latitude}, {obj.longitude}"
    location.short_description = 'Location'

# -------------------------------
# Register models
# -------------------------------
admin.site.register(Alert, AlertAdmin)
admin.site.register(Report, ReportAdmin)
