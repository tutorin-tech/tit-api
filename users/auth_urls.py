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

"""URL configuration for the users application. """

from django.urls import re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import SetPasswordView, SignUpView, WhoAmIView

urlpatterns = [
    re_path('set-password/?$', SetPasswordView.as_view(), name='set-password'),
    re_path('signup/?$', SignUpView.as_view(), name='sign-up'),
    re_path('token/?$', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    re_path('token/refresh/?$', TokenRefreshView.as_view(), name='token-refresh'),
    re_path('whoami/?$', WhoAmIView.as_view(), name='who-am-i')
]
