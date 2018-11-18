
# Complete configuration file
# Want any change make here
# Don't touch base.py, dev.py or prod.py unnecessarily

SETUP = "DEVELOPMENT"   #DEVELOPMENT/PRODUCTION

AUTH_USER_MODEL = "accounts.User"

REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
                    'rest_framework.authentication.TokenAuthentication',
                    'rest_framework.authentication.SessionAuthentication'
                ),
        'DEFAULT_FILTER_BACKENDS': (
                    'django_filters.rest_framework.DjangoFilterBackend',
                    'rest_framework.filters.SearchFilter',
                ),
        'DEFAULT_METADATA_CLASS': 'rest_framework.metadata.SimpleMetadata',
        'EXCEPTION_HANDLER': 'factory.custom_exception.custom_exception_handler',
    }



EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'sendgrid_username'
EMAIL_HOST_PASSWORD = 'sendgrid_password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_SENDER = 'sender_email'


SLACK_CHANNEL = 'https://hooks.slack.com/services/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',

TWILIO_ACCOUNT_SID = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
TWILIO_AUTH_TOKEN = 'your_auth_token'
SMS_SENDER = "sender_mobile_number" #with country code

