from django.contrib import admin
from network.models import Network



@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    # Поля, которые показываются в списке
    list_display = ['name', 'email', 'city', 'supplier', 'debt', 'created_at']
    # Фильтр по городу
    list_filter = ['city']
    # Admin action для очистки задолженности
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        # Обнуляем долг у всех выбранных объектов
        queryset.update(debt=0)

    # Название действия в админке
    clear_debt.short_description = 'Очистить задолженность'




