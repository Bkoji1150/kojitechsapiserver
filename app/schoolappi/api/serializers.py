from rest_framework import serializers 
from schoolappi.models import Student, Course, Teacher, Review, Payment
from django.utils.timezone import now


class PaymentSerializer(serializers.ModelSerializer):
    # payment_user = serializers.StringRelatedField(read_only=True)
    class Meta: 
        model = Payment
        exclude = ('payment_user',)

class StudentListSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()
    confirm_user = PaymentSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        exclude = ('total_amount_paid','number_of_payment','status', 'student_balance' )

    def get_days_since_joined(self, object):
        return (now() - object.created_date).days

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude = ('course',)
        # fields = '__all__'           

class TeacherListSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField() 
    
    class Meta:
        model = Teacher
        exclude = ('course_name',)

    def get_days_since_joined(self, object):
        return (now() - object.created_date).days

class CourseListSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True, read_only=True)
    student = StudentListSerializer(many=True, read_only=True)
    teacher = TeacherListSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
