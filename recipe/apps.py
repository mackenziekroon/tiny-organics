from django.apps import AppConfig


class RecipeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipe'

class AllergenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'allergen'

class CustomerCongif(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer'
