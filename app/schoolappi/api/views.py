
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from schoolappi.api.permissions import (IsAdminOrReadOnly, ReviewUserOrReadOnly)
from schoolappi.models import (Course, Student, Teacher, Review, Payment)
from schoolappi.api.serializers import (StudentListSerializer, CourseListSerializer,
                                         TeacherListSerializer, ReviewSerializer, PaymentSerializer)
from rest_framework import viewsets
# from rest_framework import mixins
from rest_framework import generics
from rest_framework.exceptions import ValidationError
## COURSE VIEWSETS
"""
USING ROUTER  VIEW-SET
# """
# class StudentsInKojitechs(viewsets.ViewSet):
#     permission_classes = [IsAdminOrReadOnly]
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#     def list(self, request):
#         queryset = Student.objects.all()
#         serializer = StudentListSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Student.objects.all()
#         student = get_object_or_404(queryset, pk=pk)
#         serializer = StudentListSerializer(student)
#         return Response(serializer.data)
        
#     def create(self, request):
#         serializer = StudentListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
"""
USING ROUTER  ModelVIEW-SET FOR STUDENTS
# """  


"""
USING ROUTER  VIEW-SET
# """
# class CoursesInKojitechs(viewsets.ViewSet):
#     permission_classes = [IsAdminOrReadOnly]
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#     def list(self, request):
#         queryset = Course.objects.all()
#         serializer = CourseListSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Course.objects.all()
#         course = get_object_or_404(queryset, pk=pk)
#         serializer = CourseListSerializer(course)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = CourseListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     
# """
# USING ROUTER  ModelVIEW-SET FOR STUDENTS
# """  
class CoursesInKojitechs(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    # permission_classes = [IsAdminOrReadOnly]


# """
# USING GENERIC CLASS-BASED VIEWS 
# """

class CourseList(generics.ListCreateAPIView):
    serializer_class = CourseListSerializer
    queryset = Course.objects.all()
    
# class CourseList(APIView):
    
#     def get(self, request):
#         course = Course.objects.all()
#         serializer = CourseListSerializer(course, many=True, context={'request': request})
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CourseListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


"""
USING GENERIC CLASS-BASED VIEWS 
"""
# class CourseDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseListSerializer
#     permission_classes = [IsAdminOrReadOnly]



# class CourseDetails(APIView):
#     def get(self, request, pk):
#         try:
#             course = Course.objects.get(pk=pk)
#             serializer = CourseListSerializer(course)
#             return Response(serializer.data)    
#         except Course.DoesNotExist:
#             error = {
#                 'error': 'course does\'t exist'
#             }
#             return Response(error, status=status.HTTP_404_NOT_FOUND)  

#     def put(self, request, pk):
#         course = Course.objects.get(pk=pk)
#         serializer = CourseListSerializer(course, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

#     def delete(self, request, pk):
#         course = Course.objects.get(pk=pk)
#         course.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class StudentsInKojitechs(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer 
    # permission_classes = [IsAdminOrReadOnly]
"""
USING GENERIC CLASS-BASED VIEWS StudentList
"""
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer

# class StudentList(APIView):

#     def get(self, request):
#         student = Student.objects.all()
#         serializer = StudentListSerializer(student, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = StudentListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
USING GENERIC CLASS-BASED VIEWS StudentList
"""

# class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentListSerializer
#     permission_classes = [IsAdminOrReadOnly]


# class PaymentsDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentListSerializer
#     permission_classes = [IsAdminOrReadOnly]
# class StudenDetails(APIView):
#     def get(self, request, pk):
#         try:
#             student = Student.objects.get(pk=pk)
#             serializer = StudentListSerializer(student, context={'request': request})
#             return Response(serializer.data)    
#         except Student.DoesNotExist:
#             error = {
#                 'error': 'student does not exist'
#             }
#             return Response(error, status=status.HTTP_404_NOT_FOUND)  

#     def put(self, request, pk):
#         student = Student.objects.get(pk=pk)
#         serializer = StudentListSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

#     def delete(self, request, pk):
#         student = Student.objects.get(pk=pk)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

"""
USING GENERIC CLASS-BASED VIEWS 
"""

class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListSerializer
 
    # permission_classes = [permissions.IsAuthenticated]


# ## TEACHERS VIEWSETS
# class TeachersList(APIView):
    
#     def get(self, request):
#         teacher = Teacher.objects.all()
#         serializer = TeacherListSerializer(teacher, many=True, context={'request': request})
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = TeacherListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

"""
USING GENERIC CLASS-BASED VIEWS StudentList
"""
# class TeachersInKojitechs(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherListSerializer
#     permission_classes = [AdminOrReadOnly]

# class TeacherDetails(generics.RetrieveUpdateDestroyAPIView):
#     parser_classes = [IsAdminOrReadOnly]
#     serializer_class = TeacherListSerializer
#     queryset = Teacher.objects.all()

class TeacherDetails(APIView):
    parser_classes = [IsAdminOrReadOnly]
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



# ## REVIEW VIEWSETS
# class ReviewList(APIView):
    
#     def get(self, request):
#         reviews = Review.objects.all()
#         serializer = ReviewSerializer(reviews, many=True, context={'request': request})
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

# class ReviewDetails(APIView):
#     def get(self, request, pk):
#         try:
#             review = Review.objects.get(pk=pk)
#             serializer = ReviewSerializer(review)
#             return Response(serializer.data)    
#         except review.DoesNotExist:
#             error = {
#                 'error': 'review does\'t exist'
#             }
#             return Response(error, status=status.HTTP_404_NOT_FOUND)  

#     def put(self, request, pk):
#         review = Review.objects.get(pk=pk)
#         serializer = ReviewSerializer(review, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

#     def delete(self, request, pk):
#         review = Review.objects.get(pk=pk)
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


"""
USING MIXING
"""
# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ReviewDetails(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs) 
     

"""
USING GENERIC CLASS-BASED VIEWS 
"""
class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Review.objects.filter(course=pk)


# class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     permission_classes = [ReviewUserOrReadOnly]


class CreateReview(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [ReviewUserOrReadOnly]
    
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

class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentsDetails(APIView):
   
    def get(self, request,  *args, **kwargs):
        try:
            pk = self.kwargs.get('pk')
            payment = get_object_or_404(Payment.objects.all(), pk=pk)
            # serializer = PaymentSerializer(instance=save_allowance,data=data,partial=True)

            payment = Payment.objects.get(pk=pk)
            serializer = PaymentSerializer(payment)
            return Response(serializer.data)    
        except payment.DoesNotExist:
            error = {
                'error': 'teacher does\'t exist'
            }
            return Response(error, status=status.HTTP_404_NOT_FOUND)  

    # def put(self, request, pk):
    #     payment = Payment.objects.get(pk=pk)
    #     serializer = PaymentSerializer(payment, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

    # def delete(self, request, pk):
    #     payment = Payment.objects.get(pk=pk)
    #     payment.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    




