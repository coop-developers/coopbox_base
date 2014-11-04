from django.conf import settings
from django_jinja import library

@library.global_function
def site_config(variable_name=None):
    if variable_name:
        return getattr(settings, variable_name, None)
    else:
        return settings
