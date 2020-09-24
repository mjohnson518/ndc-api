from rest_framework import serializers
from pages.models import NDC


class NDCSerializer(serializers.ModelSerializer):
    class Meta:
        model = NDC
        fields = ('country', 'title', 'Submission_type', 'Submission_date', 'Description', 'ref_num')
