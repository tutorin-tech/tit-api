"""A module that contains the class-based views related to the courses application. """

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from rest_framework import permissions, status, views, viewsets

from .chat import Chat
from .models import Course
from .serializers import ContactUsSerializer, CourseSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):  # pylint: disable=too-many-ancestors
    """Returns both a courses list and a course. """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ContactUs(views.APIView):
    """Class-based view implementing processing data from the Contact Us modal. """

    authentication_classes = []
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        """Handles requests with a post method. """

        name = request.data.get('name', '')
        email = request.data.get('email', '')
        message = request.data.get('message', '')
        agreement = request.data.get('agreement', '')

        serializer = ContactUsSerializer(
            data={
                'name': name,
                'email': email,
                'message': message,
                'agreement': agreement,
            }
        )

        if serializer.is_valid():
            html_message = render_to_string('emails/contact_us.html', context={
                'name': name,
                'email': email,
                'message': message,
            })
            send_mail('TutorInTech', html_message, None, [settings.DEFAULT_FROM_EMAIL])

            chat = Chat(settings.ROCKET_CHAT_ROOM)
            chat.contact_us(name, email, message)

            return HttpResponse(status=status.HTTP_200_OK)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
