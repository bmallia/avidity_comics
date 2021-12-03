from django.apps import AppConfig
import os

class ComicsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.comicsApp'
    public_key = os.environ.get("COMICS_PUBLIC_KEY")
    private_key = os.environ.get("COMICS_PRIVATE_KEY")