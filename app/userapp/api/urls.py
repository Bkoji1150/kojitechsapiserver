from django.urls import path, include
# from .views import movie_list, movie_details
from .views import (ReviewList, ReviewDetails, CreateView, 
                    StudentsInKojitechs, CoursesInKojitechs,
                   TeacherList,TeacherDetails )

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
courses = DefaultRouter()
# teacher = DefaultRouter()

router.register(r'students', StudentsInKojitechs, basename='studentsinKojitechs')
courses.register(r'courses', CoursesInKojitechs, basename='coursesinKojitechs')
# teacher.register(r'teachers', TeachersInKojitechs, basename='teachersinKojitechs')
urlpatterns = [
    path('students/', include(router.urls)),
    path('', include(courses.urls), name="all-courses-list"),
    # path('teachers', include(teacher.urls), name="teachers-list" ),
    path("<int:pk>/create-review/", CreateView.as_view(), name="create-review" ),
    path("<int:pk>/reviews/", ReviewList.as_view(), name="review-list" ),
    path("reviews/<int:pk>/", ReviewDetails.as_view(), name="review-details" ),
    path("teachers/", TeacherList.as_view(), name="teachers-list" ),
    path("teachers/<int:pk>/", TeacherDetails.as_view(), name="teachers-details"),
] 
