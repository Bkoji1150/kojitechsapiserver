from django.urls import path, include
# from .views import movie_list, movie_details
from .views import (StudentList, StudentDetails, CourseList, 
                    CourseDetails, TeacherList , TeacherDetails, 
                    ReviewList, ReviewDetails, CreateView, 
                    StudentsInKojitechs, CoursesInKojitechs)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
courses = DefaultRouter()

router.register(r'students', StudentsInKojitechs, basename='studentsinKojitechs')
courses.register(r'courses', CoursesInKojitechs, basename='coursesinKojitechs')
urlpatterns = [
    # path("students/", StudentList.as_view(), name="all-students-list" ),
    # path("students/<int:pk>", StudentDetails.as_view(), name="all-students-details" ),
    path('', include(router.urls)),
    path("courses/", include(courses.urls), name="all-courses-list"),
    
    # path("courses/", CourseList.as_view(), name="course-list" ),
    # path("courses/<int:pk>", CourseDetails.as_view(), name="course-details" ),

    path("courses/<int:pk>/createreview/", CreateView.as_view(), name="review-create" ),
    path("courses/<int:pk>/reviews/", ReviewList.as_view(), name="review-list" ),
    path("courses/reviews/<int:pk>", ReviewDetails.as_view(), name="review-details" ),

    path("teachers/", TeacherList.as_view(), name="teachers-list" ),
    path("teachers/<int:pk>", TeacherDetails.as_view(), name="teachers-details"),
] 

