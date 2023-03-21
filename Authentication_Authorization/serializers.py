from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    reg_no = serializers.CharField(
        max_length=10, write_only=True, required=True)
    department = serializers.CharField(
        required=True, max_length=5, write_only=True)
    university = serializers.CharField(
        required=True, max_length=100, write_only=True)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()

        data_dict['reg_no'] = self.validated_data.get('reg_no', '')
        data_dict['department'] = self.validated_data.get('department', '')
        data_dict['university'] = self.validated_data.get('university', '')

        return data_dict
