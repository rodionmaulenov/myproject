from rest_framework import serializers
from .models import Person
from files.models import Document


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = [
            'id', 'in_program', 'name', 'surname', 'country', 'blood', 'blood_type',
            'cesarean', 'children', 'is_public', 'date_update', 'date_create',
            'document', 'limit_set', 'get_days_in_ukr', 'get_days_when_date_update',
        ]
        read_only_fields = [
            'document', 'limit_set'
        ]

    def create(self, validated_data):
        person = Person.objects.create(**validated_data)
        Document.objects.create(person=person)
        return person




