from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(ChillVariations)
admin.site.register(Guide)
admin.site.register(Pricing)
admin.site.register(Priority)
admin.site.register(RatingPlace)
admin.site.register(Region)


@admin.register(Avilable)
class AvilableAdmin(admin.ModelAdmin):
    list_display = ('isAvilable', 'Region_id')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_filter = ('Priority_id', 'Avilable_id')
    list_display = ('title', 'descriptions', 'Priority_id', 'Pricing_id', 'Avilable_id')


@admin.register(TaskDate)
class TaskDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'dateIn', 'dateOut')


@admin.register(TaskTime)
class TaskDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'timeIn', 'timeOut')
