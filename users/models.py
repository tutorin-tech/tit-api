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

"""A module that contains models for the users application. """

import binascii
import os

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Person(models.Model):
    """Extends the User model. """

    user = models.OneToOneField(User, models.CASCADE)
    account_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'


class AccountConfirmationToken(models.Model):
    """The token for account confirmation. """

    person = models.OneToOneField(Person, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    token = models.CharField(db_index=True, unique=True, max_length=8)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = binascii.hexlify(os.urandom(4)).decode()

        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.token}'
