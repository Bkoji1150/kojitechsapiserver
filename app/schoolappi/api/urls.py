from django.urls import path, include
# from .views import movie_list, movie_details
from .views import StudentList, StudenDetails, CourseList, CourseDetails, TeachersList , TeachersDetails, ReviewList, ReviewDetails

urlpatterns = [
    path("students/", StudentList.as_view(), name="all-students-list" ),
    path("students/<int:pk>", StudenDetails.as_view(), name="all-students-details" ),
    path("courses/", CourseList.as_view(), name="course-list" ),
    path("courses/<int:pk>", CourseDetails.as_view(), name="course-details" ),
    path("courses/reviews/", ReviewList.as_view(), name="review-list" ),
    path("courses/reviews/<int:pk>", ReviewDetails.as_view(), name="review-details" ),
    path("teachers/", TeachersList.as_view(), name="teachers-list" ),
    path("teachers/<int:pk>", TeachersDetails.as_view(), name="teachers-details"),
] 

