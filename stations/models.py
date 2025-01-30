from django.db import models
from django.utils.translation import gettext_lazy as _

USER_ACCESS_TOKEN_CHOICES = [("web", "Web"), ("api", "API")]
USER_ROLE_CHOICES = [("Admin", "Admin"), ("Member", "Member")]


class WeatherStations(models.Model):
    """This model stores information about weather stations
    Returns:
        class: details of weather stations
    """

    name = models.CharField(
        _("name"), help_text="Name of the weather station", max_length=255
    )
    location = models.CharField(
        _("location"),
        help_text="Location of the station (e.g., city, coordinates)",
        max_length=255,
    )
    description = models.TextField(
        _("description"), help_text="Description of the station", blank=True, null=True
    )
    created_at = models.DateTimeField(
        _("created at"),
        help_text="Timestamp of when the station was created",
        auto_now_add=True,
    )
    created_by = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.SET_NULL,
        verbose_name="created by",
        help_text="User who created the station",
        null=True,
        blank=True,
        related_name="created_stations",
        related_query_name="created_stations",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "weather station"
        verbose_name_plural = "weather stations"


class Sensors(models.Model):
    """This model stores information about sensors in weather stations
    Returns:
        class: details of sensors
    """

    station = models.ForeignKey(
        "stations.WeatherStations",
        on_delete=models.CASCADE,
        verbose_name="station",
        help_text="Weather station to which the sensor belongs",
        related_name="sensors",
        related_query_name="sensor",
    )
    name = models.CharField(_("name"), help_text="Name of the sensor", max_length=255)
    description = models.TextField(
        _("description"), help_text="Description of the sensor", blank=True, null=True
    )
    data_identifier = models.CharField(
        _("data identifier"),
        help_text="Identifier of the sensor in the station data",
        max_length=255,
    )
    units = models.CharField(
        _("units"), help_text="Units of the data acquired by the sensor", max_length=50
    )
    active = models.BooleanField(
        _("active"), help_text="If the sensor is currently active or not", default=True
    )
    last_deactivated_at = models.DateTimeField(
        _("last deactivated at"),
        help_text="Timestamp of when the sensor was deactivated",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        _("created at"),
        help_text="Timestamp of when the sensor was created",
        auto_now_add=True,
    )
    created_by = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.SET_NULL,
        verbose_name="created by",
        help_text="User who created the sensor",
        null=True,
        blank=True,
        related_name="created_sensors",
        related_query_name="created_sensor",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "sensor"
        verbose_name_plural = "sensors"


class SensorData(models.Model):
    """This model stores data recorded by sensors
    Returns:
        class: details of sensor data
    """

    sensor = models.ForeignKey(
        "stations.Sensors",
        on_delete=models.CASCADE,
        verbose_name="sensor",
        help_text="Sensor that recorded the data",
        related_name="data",
        related_query_name="datum",
    )
    data = models.DecimalField(
        _("data"),
        help_text="Data recorded by the sensor",
        max_digits=10,
        decimal_places=2,
    )
    timestamp = models.DateTimeField(
        _("timestamp"),
        help_text="Date and time when the data was recorded",
    )

    def __str__(self):
        return f"{self.sensor.name} - {self.timestamp}"

    class Meta:
        verbose_name = "sensor data"
        verbose_name_plural = "sensor data"


class StationAccessTokens(models.Model):
    """This model stores access tokens for weather stations
    Returns:
        class: details of station access tokens
    """

    station = models.ForeignKey(
        "stations.WeatherStations",
        on_delete=models.CASCADE,
        verbose_name="station",
        help_text="Weather station to which the access token belongs",
        related_name="access_tokens",
        related_query_name="access_token",
    )
    token = models.CharField(
        _("token"),
        help_text="Token string for accessing the station data",
        max_length=255,
        unique=True,
    )
    label = models.CharField(
        _("label"),
        help_text="Label for the station access token",
        max_length=255,
    )
    description = models.TextField(
        _("description"),
        help_text="Description of the station access token",
        blank=True,
        null=True,
    )
    created_by = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.SET_NULL,
        verbose_name="created by",
        help_text="User who created the access token",
        null=True,
        blank=True,
        related_name="created_tokens",
        related_query_name="created_token",
    )
    created_at = models.DateTimeField(
        _("created at"),
        help_text="Timestamp of when the access token was created",
        auto_now_add=True,
    )
    last_used_at = models.DateTimeField(
        _("last used at"),
        help_text="Timestamp of when the access token was last used",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.station.name} - {self.label}"

    class Meta:
        verbose_name = "station access token"
        verbose_name_plural = "station access tokens"
