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

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'           

class CourseListSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True, read_only=True)
    student = StudentListSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class TeacherListSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField() 
    
    class Meta:
        model = Teacher
        fields = '__all__'

    def get_days_since_joined(self, object):
        return (now() - object.created_date).days