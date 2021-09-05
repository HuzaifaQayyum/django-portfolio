from django.contrib import admin

from contact.models import *

admin.site.register(Budget)
admin.site.register(Client)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['get_client_name', 'get_client_email', 'description']
    list_display_links = ['get_client_name', 'get_client_email']

    @admin.display(ordering='name', description='name')
    def get_client_name(self, obj):
        return obj.client.name

    @admin.display(description='email')
    def get_client_email(self, obj):
        return obj.client.email
