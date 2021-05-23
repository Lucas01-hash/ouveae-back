import django_filters.rest_framework
from rest_framework import serializers, viewsets
from rest_framework import generics

from .models import Entry, EntryType, EntryTopic

# Entry - Serializers define the API representation.
class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__' 

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    filterset_fields = ('protocol',)

# EntryType - Serializers define the API representation.
class EntryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryType
        fields = ['id','name','color','icon']

class EntryTypeViewSet(viewsets.ModelViewSet):
    queryset = EntryType.objects.all()
    serializer_class = EntryTypeSerializer

# EntryTopic - Serializers define the API representation.
class EntryTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryTopic
        fields = ['id','name']

class EntryTopicViewSet(viewsets.ModelViewSet):
    queryset = EntryTopic.objects.all()
    serializer_class = EntryTopicSerializer