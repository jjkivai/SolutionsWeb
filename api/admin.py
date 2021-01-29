from django.contrib import admin
from api.models import Client, License, Message, Project, ProjectImage

# Register your models here.
class ProjectImageInstance(admin.TabularInline):
    model = ProjectImage


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "short_description"]
    inlines = [ProjectImageInstance]


class ClientAdmin(admin.ModelAdmin):
    list_display = ["company"]


class LicenseAdmin(admin.ModelAdmin):
    list_display = ["name"]


class MessageAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "company", "email"]
    readonly_fields = ["first_name", "last_name", "company", "email", "message"]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(License, LicenseAdmin)
admin.site.register(Message, MessageAdmin)
