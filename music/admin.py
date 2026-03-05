from django.contrib import admin
from .models import Section, Film, Song

admin.site.register(Section)
admin.site.register(Film)
admin.site.register(Song)


# admin.py
from django.contrib import admin
from .models import AuthBanner

@admin.register(AuthBanner)
class AuthBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']


    from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ("email", "is_staff", "is_superuser", "is_active")
    list_filter = ("is_staff", "is_superuser", "is_active")

    ordering = ("email",)
    search_fields = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "is_active", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_staff", "is_superuser"),
        }),
    )