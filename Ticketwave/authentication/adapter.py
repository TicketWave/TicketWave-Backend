from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth.hashers import make_password

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        try:
            user = super().save_user(request, user, form, commit)
            
            data = form.cleaned_data
            user.is_public = data.get('is_public')
            user.image_id = data.get('image_id')
            user.first_name = data.get('first_name')
            user.last_name = data.get('last_name')

            user.is_active = False
            user.save()
        except:
            pass
        return user

    def set_password(self, user, password):
        return super().set_password(user, make_password(password))
