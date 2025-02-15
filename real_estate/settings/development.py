from .base import *

DATABASES = {
    'default': {
        'ENGINE': env("POSTGRES_ENGINE"),
        'NAME': env("POSTRES_DB"),
        'USER': env("POSTGRES_USER"),
        'PASSWORD': env("POSTGRES_PASSWORD"),
        'HOST': env("PG_HOST"),
        'PORT': env("PG_PORT"),
    }
}