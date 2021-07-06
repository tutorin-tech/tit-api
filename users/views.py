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

"""A module that contains the class-based views related to the users application. """

from django.contrib.auth import get_user_model
from rest_framework import generics, mixins, permissions, status
from rest_framework.response import Response

from .models import Person
from .serializers import SetPasswordSerializer, SignUpSerializer

User = get_user_model()


class SetPasswordView(mixins.UpdateModelMixin, generics.GenericAPIView):
    """Sets the password when the user confirms the account. """

    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = SetPasswordSerializer

    def put(self, request, *args, **kwargs):
        """PUT-method for setting user password after signing up. """

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            person = Person.objects.get(
                accountconfirmationtoken__token=serializer.validated_data['token']
            )
            self.kwargs['pk'] = person.user.id

            self.update(request, *args, **kwargs)

        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid()  # Fake, real validation is done in put method.
        self.perform_update(serializer)

        return Response(status=status.HTTP_200_OK)


class SignUpView(mixins.CreateModelMixin, generics.GenericAPIView):
    """Creates a User model instance. """

    permission_classes = (permissions.AllowAny, )
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        """POST-method for creating new user. """

        return self.create(request, *args, **kwargs)
