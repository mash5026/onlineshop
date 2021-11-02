from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('full_name', 'email', 'is_admin', 'mobile', 'address')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'full_name', 'mobile', 'address')}),
        ('Personal Info', {'fields': ('is_active',)}),
        ('Permisions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2', 'full_name')}),
    )
    search_fields = ('mobile',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)