from django.contrib import admin
from . import models as accounts_models

# Register your models here.

models = [
            accounts_models.User,
        ]
admin.site.register(models)