"""Module helps sending messages to the Rocket.Chat. """

from django.conf import settings
from rocketchat.api import RocketChatAPI


class Chat:
    """Class for sending messages to the Rocket.Chat. """

    api = None

    def __init__(self, channel):
        Chat.api = Chat.api or RocketChatAPI(settings={'username': settings.ROCKET_CHAT_USERNAME,
                                                       'password': settings.ROCKET_CHAT_PASSWORD,
                                                       'domain': settings.ROCKET_CHAT_DOMAIN})
        self._channel = channel

    def contact_us(self, name, email, message):
        """Sends the contact us message to the Rocket.Chat. """

        Chat.api.send_message(f'Новое сообщение от {name} ({email}): {message}', self._channel)
