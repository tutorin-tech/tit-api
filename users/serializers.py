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
from rest_framework import serializers

User = get_user_model()


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
