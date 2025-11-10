from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import AccountTier, User
from .repositories import AccountTierRepository


@admin.register(AccountTier)
class AccountTierAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'daily_ai_search_limit', 'is_default')
    list_editable = ('daily_ai_search_limit', 'is_default')
    search_fields = ('name', 'code')
    ordering = ('name',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        AccountTierRepository().enforce_single_default(obj)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User

    list_display = ('email', 'account_tier', 'is_staff', 'is_superuser')
    list_filter = ('account_tier', 'is_staff', 'is_superuser')
    ordering = ('email',)
    search_fields = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('AI Search', {'fields': ('account_tier', 'ai_search_count', 'ai_search_count_reset_at')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'account_tier', 'password1', 'password2', 'is_staff', 'is_superuser'),
            },
        ),
    )
    readonly_fields = ('ai_search_count', 'ai_search_count_reset_at')
