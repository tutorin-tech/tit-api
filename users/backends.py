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

"""A module that contains custom authentication backends. """

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class CaseInsensitiveModelBackend(ModelBackend):
    """Authentication backend class that allows case-insensitive login. """

    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()

        if username is None:
            username = kwargs.get(user_model.USERNAME_FIELD)

        try:
            username_field = f'{user_model.USERNAME_FIELD}__iexact'
            # pylint: disable=protected-access
            user = user_model._default_manager.get(**{username_field: username})
        except user_model.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (see
            # https://code.djangoproject.com/ticket/20760)
            user_model().set_password(password)

            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

            return None


class EmailModelBackend(ModelBackend):
    """Authentication backend class that allows login using email and password. """

    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()

        if username is None:
            username = kwargs.get(user_model.EMAIL_FIELD)

        try:
            email_field = f'{user_model.EMAIL_FIELD}__iexact'
            # pylint: disable=protected-access
            user = user_model._default_manager.get(**{email_field: username})
        except user_model.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (see
            # https://code.djangoproject.com/ticket/20760)
            user_model().set_password(password)

            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

            return None
