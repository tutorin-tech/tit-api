# Copyright 2021 Denis Gavrilyuk. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and

"""A module that contains the signals for the users application. """

from urllib.parse import urljoin

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import AccountConfirmationToken, Person

User = get_user_model()


@receiver(post_save, sender=User)
def create_person(sender,  # pylint: disable=unused-argument
                  instance, created, **_kwargs):
    """Creates a Person instance and sends an email to the user, letting them to confirm
    their email address. """

    if created:
        person = Person.objects.create(user=instance)
        ac_token = AccountConfirmationToken.objects.create(person=person)

        confirm_account_base_url = urljoin(settings.BASE_SITE_URL, '/confirm-account/')
        context = {
            'confirm_account_url': f'{confirm_account_base_url}?token={ac_token.token}',
        }
        email_html_message = render_to_string('emails/confirm_account.html', context)

        msg = EmailMultiAlternatives(
            subject='Подтверждение регистрации',
            from_email=settings.DEFAULT_FROM_EMAIL,
            bcc=[instance.email],
            headers={
                'From': f'{settings.DEFAULT_SITE_NAME} <{settings.DEFAULT_FROM_EMAIL}>',
                'To': instance.email,
            }
        )

        msg.attach_alternative(email_html_message, 'text/html')
        msg.send()
