
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from rest_framework import viewsets
# from rest_framework import mixins
from rest_framework import generics
from rest_framework.exceptions import ValidationError
## COURSE VIEWSETS
"""
USING ROUTER  VIEW-SET
"""

# class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     # permission_classes = [ReviewUserOrReadOnly]


# class CreateView(generics.CreateAPIView):
#     serializer_class = ReviewSerializer
#     permission_classes = [ReviewUserOrReadOnly]
    
#     def get_queryset(self):
#         return Review.objects.all()
    
#     def perform_create(self, serializer):
#         pk = self.kwargs.get('pk')
#         course = Course.objects.get(pk=pk)
 
#         review_user = self.request.user
#         review_queryset = Review.objects.filter(course=course,review_user=review_user )

#         if review_queryset.exists():
#             raise ValidationError("You already have a review for this course") 

#         if course.number_of_rating == 0:
#             course.avg_rating = serializer.validated_data['rating']
#         else:
#             course.avg_rating=(course.avg_rating + serializer.validated_data['rating']) / 2 

#         course.number_of_rating = course.number_of_rating + 1
#         course.save()
#         serializer.save(course=course, review_user=review_user)



