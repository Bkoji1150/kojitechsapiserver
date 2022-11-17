
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from schoolappi.api.throttling import ReviewCreateThrottle, ReviewDeleteThrottle
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from schoolappi.api.permissions import (IsAdminOrReadOnly, IsReviewUserOrReadOnly)
from schoolappi.models import (Course, Student, Teacher, Review, Payment)
from schoolappi.api.serializers import (StudentListSerializer, CourseListSerializer,
                                         TeacherListSerializer, ReviewSerializer, PaymentSerializer)
from schoolappi.api.pagination import (CoursePagination,  CourseListLOPagination,  StudentWatchListCPagination)                                       


from rest_framework import viewsets
from rest_framework import generics
from rest_framework.exceptions import ValidationError

class UserReview(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        return Review.objects.filter(review_user__username=username)

class CreateReview(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    pagination_classes = [CoursePagination]
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        course = Course.objects.get(pk=pk)
 
        review_user = self.request.user
        review_queryset = Review.objects.filter(course=course,review_user=review_user )

        if review_queryset.exists():
            raise ValidationError("You already have a review for this course") 

        if course.number_of_rating == 0:
            course.avg_rating = serializer.validated_data['rating']
        else:
            course.avg_rating=(course.avg_rating + serializer.validated_data['rating']) / 2 

        course.number_of_rating = course.number_of_rating + 1
        course.save()
        serializer.save(course=course, review_user=review_user)

class StudentName(generics.ListAPIView):
    serializer_class = StudentListSerializer
    pagination_classes = [CoursePagination]
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):

        first_name = self.kwargs['first_name'].lower()

        return Student.objects.filter(first_name=first_name)
        
class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserOrReadOnly]
    # throttle_classes = [ReviewDeleteThrottle, ReviewCreateThrottle]
    pagination_classes = [CoursePagination]

    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['review_user__username', 'active']

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Review.objects.filter(course=pk)

class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserOrReadOnly]

class CoursesInKojitechs(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    permission_classes = [IsAdminOrReadOnly]

class CourseList(generics.ListCreateAPIView):
    serializer_class = CourseListSerializer
    queryset = Course.objects.all()
    pagination_classes = [CourseListLOPagination]


class StudentDetails(APIView):
    pagination_classes = [CoursePagination]
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentListSerializer(student)
            return Response(serializer.data)    
        except Student.DoesNotExist:
            error = {
                'error': 'student does\'t exist'
            }
            return Response(error, status=status.HTTP_404_NOT_FOUND)  

    def put(self, request, pk):
        student = Student.objects.get(pk=pk)
        serializer = StudentListSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

    def delete(self, request, pk):
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StudentList(APIView):
    permission_classes = [IsAdminOrReadOnly]
    pagination_classes = [CourseListLOPagination]
    def get(self, request):
        student = Student.objects.all()
        serializer = StudentListSerializer(student, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherList(generics.ListCreateAPIView):
    pagination_classes = [CoursePagination]
    permission_classes = [IsAdminOrReadOnly]
    queryset = Teacher.objects.all()
    serializer_class = TeacherListSerializer
 
class TeacherDetails(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request, pk):
        
        try:
            teacher = Teacher.objects.get(pk=pk)
            serializer = TeacherListSerializer(teacher)
            return Response(serializer.data)    
        except teacher.DoesNotExist:
            error = {
                'error': 'teacher does\'t exist'
            }
            return Response(error, status=status.HTTP_404_NOT_FOUND)  

    def put(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        serializer = TeacherListSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

    def delete(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PaymentList(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class Makepayment(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    pagination_classes = [CoursePagination]
    
    def get_queryset(self):
        return Payment.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        student = Student.objects.get(pk=pk)

        if student.number_of_payment != 0:
            student.total_amount_paid = student.total_amount_paid - serializer.validated_data['amount_paid'] 
            student.student_balance =  float(1000) - student.total_amount_paid
        if student.number_of_payment == float(1000):
            student.status = "completed"
            raise ValidationError("congratulation you have made a complete payment") 
        student.number_of_payment =  student.number_of_payment  + 1
        student.save()    
        if serializer.is_valid():
            serializer.save(payment_user=student) 
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
   


       

