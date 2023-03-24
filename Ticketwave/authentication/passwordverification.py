from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


User = get_user_model()

class password_TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )


password_TokenGenerator = password_TokenGenerator()


@api_view(('GET', 'POST'))
@permission_classes((AllowAny,))
def send_password_reset_email(request: Request, username, useremail):
    try:
        user = User.objects.get(email=useremail)
        if user.username != username:
            user = None
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None:
        try:

            mail_subject = 'Activate your user account.'

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = password_TokenGenerator.make_token(user)
            email = EmailMessage(
                mail_subject, f'your new password is {uid}{token}, please change it as soon as possible', to=[user.email])

            if email.send():
                try:
                    user.password = make_password(uid+token)
                    user.save()
                except:
                    email = EmailMessage(
                        mail_subject, f'a database error happened please submit a new password reset request', to=[user.email])
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=400)
        except:
            print('exception thrown')

    return HttpResponse(status=400)
