# Apps introduced by Django
DJANGO_APPS = [
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
            ]

# THIRD PARTY APPS
THIRD_PARTY_APPS = [
                        'rest_framework',
                        'django_filters',
                        'rest_framework_swagger',
                    ]

# Apps created by you in this project
CREATED_APPS = [
                    'accounts',
                    'factory',
                ]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + CREATED_APPS

