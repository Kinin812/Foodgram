from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from foodgram.settings import EMPTY_MSG
from users.models import CustomUser

from .forms import CustomUserChangeForm, CustomUserCreationForm

admin.site.unregister(Group)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        'id', 'username', 'email', 'first_name',
        'last_name', 'is_active', 'is_admin', 'is_superuser',
    )
    list_filter = ('username', 'email',)
    fieldsets = (
        (None, {'fields': (
            'username', 'email', 'first_name', 'last_name', 'password'
        )}),
        ('Права', {'fields': ('is_active', 'is_admin',)}),
    )
    empty_value_display = EMPTY_MSG
    list_display_links = ('username',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'first_name',
                'last_name', 'password1', 'password2'
            )
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('id',)
