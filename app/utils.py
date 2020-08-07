from django.conf import settings
import messagebird


def send_message(phonenumber,message):
    client = messagebird.Client(settings.ACCESS_KEY)
    message = client.message_create(
        'MessageBird',
        '31XXXXXXXXX',
        'Hi! This is your first message',
        {'reference': 'Foobar'}
    )
