from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    """ Пользователи """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'surname', 'name', 'patronymic', 'is_staff',)
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('surname', 'name', 'patronymic', 'email', 'phone', 'date_of_birth', 'photo',)}),
        ('Разрешения', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email', 'name', 'surname', 'patronymic')
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.site_title = 'Панель Админимтратора Отеля'
admin.site.site_header = 'Панель Администратора Отеля'
