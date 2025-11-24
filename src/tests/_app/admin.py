from django.contrib import admin


class AdminActionsTestModelAdmin(admin.ModelAdmin):
    list_display = ("name",)
