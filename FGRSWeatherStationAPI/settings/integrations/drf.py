REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "FGRSWeatherStationAPI.settings.custom_DRF_settings.renderers.UJSONRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "FGRSWeatherStationAPI.settings.custom_DRF_settings.parsers.UJSONParser",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "FGRSWeatherStationAPI.settings.custom_DRF_settings.authentication.TokenAuthentication",
    ],
}
