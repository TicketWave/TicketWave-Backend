from django.http.response import HttpResponse
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.request import Request
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class Email_Activation_TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )


Email_Activation_Token = Email_Activation_TokenGenerator()


@api_view(('GET', 'POST'))
@permission_classes((AllowAny,))
def send_verification_email(request: Request, user_pk):
    print(request.data)
    try:
        user = User.objects.get(id=user_pk)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None:
        try:

            mail_subject = 'Activate your user account.'

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = Email_Activation_Token.make_token(user)
            email = EmailMessage(
                mail_subject, f'please click on the link to verify your email http://localhost:8000/auth/activate_email/{uid}/{token}/', to=[user.email])

            if email.send():
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=400)
        except:
            print('exception thrown')

    return HttpResponse(status=400)


def activate_email(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=uid)

    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and Email_Activation_Token.check_token(user, token):
        user.is_active = True
        user.save()
        EmailMessage('Ticket wave email verification',
                     'Thank you for your email confirmation. your email has been verified.', to=[user.email])
        return HttpResponse(status=200)
    else:
        if user is not None:
            EmailMessage('Ticket wave email verification',
                         'Activation link is invalid! or another error occured', to=[user.email])
            return HttpResponse(status=400)
        else:
            return HttpResponse(status=400)
