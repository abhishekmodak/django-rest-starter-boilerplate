
from django.apps import apps
from django.contrib import admin

def ready():
    models = apps.get_models()
    print("aaaaaaaaaaaaaaaa")
    print(models)
    for model in models:
        try:
            admin.site.register(model)
        except admin.sites.AlreadyRegistered:
            pass
