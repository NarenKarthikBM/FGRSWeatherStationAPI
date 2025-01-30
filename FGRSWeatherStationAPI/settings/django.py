from .env import env

DEBUG = env.bool("DEBUG", default=True)
TEMPLATE_DEBUG = DEBUG

if DEBUG:
    INTERNAL_IPS = ["127.0.0.1"]

SECRET_KEY = env.str(
    "SECRET_KEY",
    default="j8iv3zyqzx=%3g820(6wd#ira-p%r90$)r7v#7@wm!n3!bz=8x",
)

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "users",
    "stations",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

AUTH_USER_MODEL = "members.CustomUser"

ROOT_URLCONF = "FGRSWeatherStationAPI.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

DATABASES = {
    "default": env.db_url(
        "DATABASE_URL",
        default="mysql://USER:PASSWORD@HOST:2000/NAME",
    ),
}

WSGI_APPLICATION = "FGRSWeatherStationAPI.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ADMINS = [x.split(":") for x in env.list("DJANGO_ADMINS", default="")]

AUTH_USER_MODEL = "users.CustomUser"

STATIC_URL = "/static/"
STATIC_ROOT = "static"

# STORAGES = {
#     "staticfiles": {
#         "BACKEND": "django_s3_storage.storage.StaticS3Storage",
#     },
#     "default": {
#         "BACKEND": "django_s3_storage.storage.S3Storage",
#     },
# }
