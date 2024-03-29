from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    is_public = serializers.BooleanField(write_only=True, required=True)
    image_id = serializers.IntegerField(
        # required=True,
        write_only=True, default=1)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        
        data_dict['first_name'] = self.validated_data.get('first_name', '')
        data_dict['last_name'] = self.validated_data.get('last_name', '')
        data_dict['is_public'] = self.validated_data.get('is_public', '')
        data_dict['image_id'] = self.validated_data.get('image_id', '')

        return data_dict
