from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from job.models import Job


class AddJobSerializer(serializers.ModelSerializer):
    """
    Kasb qo'shish serializeri
    """
    class Meta:
        model = Job
        fields = ('id', 'title', 'salary')

    def validate(self, attrs):
        title: str = attrs.get('title')

        if not title.startswith('A'):
            raise ValidationError({'title': 'Kasbning bosh harfi A harfi bilan boshlanmagan'})

        return attrs
