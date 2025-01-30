from django.contrib import admin

from . import models


@admin.register(models.WeatherStations)
class WeatherStationsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "description",
        "created_at",
        "created_by",
    )
    search_fields = (
        "name",
        "location",
        "description",
        "created_by__email",
    )
    list_filter = (
        "created_at",
        "created_by",
    )
    ordering = (
        "name",
        "created_at",
    )
    list_per_page = 20
    list_max_show_all = 1000
    list_select_related = ("created_by",)
    autocomplete_fields = ("created_by",)


@admin.register(models.StationAccessTokens)
class StationAccessTokensAdmin(admin.ModelAdmin):
    list_display = (
        "station",
        "token",
        "label",
        "description",
        "created_at",
        "last_used_at",
    )
    search_fields = (
        "station__name",
        "token",
        "label",
        "description",
    )
    list_filter = (
        "created_at",
        "last_used_at",
    )
    ordering = (
        "station",
        "created_at",
    )
    list_per_page = 20
    list_max_show_all = 1000
    list_select_related = (
        "station",
        "created_by",
    )
    autocomplete_fields = (
        "station",
        "created_by",
    )


@admin.register(models.Sensors)
class SensorsAdmin(admin.ModelAdmin):
    list_display = (
        "station",
        "name",
        "data_identifier",
        "units",
        "active",
    )
    search_fields = (
        "station__name",
        "name",
        "description",
        "data_identifier",
        "units",
        "created_by__email",
    )
    list_filter = (
        "active",
        "created_at",
        "last_deactivated_at",
        "created_by",
    )
    ordering = (
        "station",
        "name",
        "created_at",
    )
    list_per_page = 20
    list_max_show_all = 1000
    autocomplete_fields = (
        "station",
        "created_by",
    )


@admin.register(models.SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = (
        "sensor",
        "data",
        "timestamp",
    )
    search_fields = (
        "sensor__name",
        "value",
    )
    ordering = (
        "sensor",
        "timestamp",
    )
    list_per_page = 20
    list_max_show_all = 1000
    list_select_related = ("sensor",)
    autocomplete_fields = ("sensor",)
