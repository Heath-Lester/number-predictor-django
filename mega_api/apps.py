"""File containing the Mega API Application configuration"""
from django.apps import AppConfig


class MegaApiConfig(AppConfig):
    """Mega API Application Config"""
    default_auto_field: str = 'django.db.models.BigAutoField'
    name: str = 'mega_api'
