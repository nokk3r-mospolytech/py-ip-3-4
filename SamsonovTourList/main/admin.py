from django.contrib import admin
from .models import *

# Register your models here.


def isAvilableFalse(modeladmin, request, queryset):
    queryset.update(isAvilable='Нет')

def isAvilableTrue(modeladmin, request, queryset):
    queryset.update(isAvilable='Да')


isAvilableFalse.short_description = "Сделать выделенным Нет"
isAvilableTrue.short_description = "Сделать выделенным Да"
admin.site.register(ChillVariations)
admin.site.register(Pricing)
admin.site.register(Region)


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_filter = ('rating', 'Region_id')
    list_display = ('name', 'rating', 'Region_id')


@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('priority', 'TaskDate_id')


@admin.register(RatingPlace)
class RatingPlaceAdmin(admin.ModelAdmin):
    list_display = ('rating_index', 'Task_id')


@admin.register(Avilable)
class AvilableAdmin(admin.ModelAdmin):
    list_display = ('isAvilable', 'Region_id')
    actions = [isAvilableFalse, isAvilableTrue]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_filter = ('Priority_id', 'Avilable_id')
    list_display = ('title', 'descriptions', 'Priority_id', 'Pricing_id', 'Avilable_id')


@admin.register(TaskDate)
class TaskDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'dateIn', 'dateOut', 'TaskTime_id')


@admin.register(TaskTime)
class TaskDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'timeIn', 'timeOut')
