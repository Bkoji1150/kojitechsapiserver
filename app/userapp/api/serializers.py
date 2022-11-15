from rest_framework import serializers 
from schoolappi.models import Student, Course, Teacher, Review
from django.utils.timezone import now

class StudentListSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField() 
    class Meta:
        model = Student
        fields = '__all__'

    def get_days_since_joined(self, object):
        return (now() - object.created_date).days
