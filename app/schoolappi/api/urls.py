from django.urls import path, include
# from .views import movie_list, movie_details
from .views import (ReviewList, CreateReview, StudentList, PaymentList, StudentDetails,
                    CoursesInKojitechs,
                   TeacherList,TeacherDetails, Makepayment , StudentName ,UserReview)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'courses', CoursesInKojitechs, basename='studentsinKojitechs')

urlpatterns = [
    path('students/', StudentList.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetails.as_view(), name='student-detail'),    

    path('students/<int:pk>/amountpaid/', PaymentList.as_view(), name='paymentdetails'),
    path('students/<int:pk>/makepayment/', Makepayment.as_view(), name='makepayments'),

    path('', include(router.urls)),
    path("courses/<int:pk>/create-review/", CreateReview.as_view(), name="create-review" ),
    path("courses/<int:pk>/reviews/", ReviewList.as_view(), name="review-list" ),
    path("teachers/", TeacherList.as_view(), name="teachers-list" ),
    path("teachers/<int:pk>/", TeacherDetails.as_view(), name="teachers-details"),

    path('search/<str:first_name>/', StudentName.as_view(), name='search-by-first-name'),
    path('user-reviews/', UserReview.as_view(), name='user-review-detail'),
    # path('search-users/', StudentName.as_view(), name='search-detail'),
] 