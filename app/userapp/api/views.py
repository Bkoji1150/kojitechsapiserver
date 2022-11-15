
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from schoolappi.api.permissions import (AdminOrReadOnly, ReviewUserOrReadOnly)
from schoolappi.models import Course, Student, Teacher, Review
from schoolappi.api.serializers import (StudentListSerializer, CourseListSerializer,
                                         TeacherListSerializer, ReviewSerializer)
from rest_framework import viewsets
# from rest_framework import mixins
from rest_framework import generics
from rest_framework.exceptions import ValidationError
## COURSE VIEWSETS
"""
USING ROUTER  VIEW-SET
"""
# 


