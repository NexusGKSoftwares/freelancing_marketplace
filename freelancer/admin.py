from django.contrib import admin
from .models import Freelancer, Job, Notification, Feedback, Payment

admin.site.register(Freelancer)
admin.site.register(Job)
admin.site.register(Notification)
admin.site.register(Feedback)

class FreelancerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('freelancer', 'amount', 'status', 'date')
    list_filter = ('status', 'date')
    search_fields = ('freelancer__name', 'transaction_id')