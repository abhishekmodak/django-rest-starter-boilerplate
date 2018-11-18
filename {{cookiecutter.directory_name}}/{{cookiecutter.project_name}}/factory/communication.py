import requests
import json
from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import Client



def send_single_mail(data):
    """ For Sending mail
    """

    result = send_mail(
                    data.get('subject', ''),
                    data.get('body', ''),,
                    settings.EMAIL_SENDER,
                    data.get('recipients', ''),
                    fail_silently=False
                )
    return 'success'



def send_slack_data(title, message):
    """ For sending messages in slack
    """

    header = {
                "Content-Type": "application/x-www-form-urlencoded",
            }

    body= {
        'text': message,
        'username': title,
        }

    req = requests.post(
                settings.SLACK_CHANNEL,
                headers=header,
                data=json.dumps(body)
            )
    return 'success'


def send_sms(body, recipient):
    """ For sending SMS
    """

    client = Client(
                        settings.TWILIO_ACCOUNT_SID,
                        settings.TWILIO_AUTH_TOKEN
                    )

    message = client.messages.create(
                              from_= settings.SMS_SENDER,
                              body='body',
                              to=recipient
                          )

    print(message.sid)
    return 'success'