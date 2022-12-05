from rest_framework import serializers
from .models import Limit


class LimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Limit
        fields = [
            'id', 'entry', 'exit', 'date_update', 'person'
        ]




