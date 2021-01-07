from django.contrib.auth import get_user_model
from rest_framework import serializers
from pages.models import NDC


class NDCSerializer(serializers.ModelSerializer):

    class Meta:
        model = NDC
        fields = '__all__'
        #('country', 'title', 'Submission_type', 'Submission_date', 'Description', 'ref_num')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('country_code', 'username',)
