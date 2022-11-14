
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from schoolappi.models import Course, Student, Teacher, Review
from schoolappi.api.serializers import (StudentListSerializer, CourseListSerializer,
                                         TeacherListSerializer, ReviewSerializer)

# from rest_framework import mixins
from rest_framework import generics
## COURSE VIEWSETS

"""
USING GENERIC CLASS-BASED VIEWS 
"""

class CourseList(generics.ListCreateAPIView):
    serializer_class = CourseListSerializer
    queryset = Course.objects.all()
    # permission_classes = [permissions.IsAuthenticated]


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
class CourseDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer



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
 
"""
USING GENERIC CLASS-BASED VIEWS StudentList
"""
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer

    # permission_classes = [permissions.IsAuthenticated]

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

class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer

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
    serializer_class = TeacherListSerializer
    queryset = Teacher.objects.all()
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

class TeacherDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherListSerializer
    queryset = Teacher.objects.all()

# class TeachersDetails(APIView):
#     def get(self, request, pk):
#         try:
#             teacher = Teacher.objects.get(pk=pk)
#             serializer = TeacherListSerializer(teacher)
#             return Response(serializer.data)    
#         except teacher.DoesNotExist:
#             error = {
#                 'error': 'teacher does\'t exist'
#             }
#             return Response(error, status=status.HTTP_404_NOT_FOUND)  

#     def put(self, request, pk):
#         teacher = Teacher.objects.get(pk=pk)
#         serializer = TeacherListSerializer(teacher, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

#     def delete(self, request, pk):
#         teacher = Teacher.objects.get(pk=pk)
#         teacher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



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
class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
