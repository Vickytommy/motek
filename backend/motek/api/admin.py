from django.contrib import admin
from .models import RegisteredUser

@admin.register(RegisteredUser)
class RegisteredUserAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "mobile", "mail", "city", "number_of_tickets")
    search_fields = ("firstname", "lastname", "mobile", "mail", "id_card")
    list_filter = ("city", "number_of_tickets")
    ordering = ("firstname", "lastname")