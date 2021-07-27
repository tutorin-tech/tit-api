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

"""A module that contains serializers for the users application. """

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import AccountConfirmationToken

User = get_user_model()


class SetPasswordSerializer(serializers.Serializer):  # pylint: disable=abstract-method
    """Serializes the set password view data. """

    token = serializers.CharField(min_length=8, max_length=8)
    password = serializers.CharField()
    retype_password = serializers.CharField()

    def validate_token(self, value):  # pylint: disable=no-self-use
        """Validates the account confirmation token. """

        if not AccountConfirmationToken.objects.filter(token=value).exists():
            raise serializers.ValidationError('Токен не найден')

        return value

    def validate_password(self, value):  # pylint: disable=no-self-use
        """Validates the new password. """

        try:
            validate_password(value)
        except ValidationError as err:
            raise serializers.ValidationError(err.messages)

        return value

    def validate_retype_password(self, value):
        """Validates the password retype. """

        if self.initial_data['password'] != value:
            raise serializers.ValidationError('Пароли на совпадают')

        return value

    def update(self, instance, validated_data):  # pylint: disable=no-self-use
        instance.set_password(validated_data['password'])
        instance.save()

        instance.person.account_confirmed = True
        instance.person.save(update_fields=['account_confirmed'])

        return instance


class SignUpSerializer(serializers.Serializer):  # pylint: disable=abstract-method
    """Serializes the signup view data. """

    username = serializers.CharField()
    email = serializers.EmailField()

    def validate_username(self, value):  # pylint: disable=no-self-use
        """Validates the username. """

        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError('Пользователь с таким именем уже существует')

        return value

    def validate_email(self, value):  # pylint: disable=no-self-use
        """Validates the username. """

        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError('Пользователь с таким email-адресом уже существует')

        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CurrentUserSerializer(serializers.ModelSerializer):
    """Serializes the username of the authenticated user for the whoami endpoint. """

    class Meta:
        model = User
        fields = ('username', )
