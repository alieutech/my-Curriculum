from rest_framework import serializers
from .models import Curriculum, Section

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'title', 'content']

class CurriculumSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = Curriculum
        fields = ['id', 'title', 'description', 'owner', 'shared_with', 'sections']
