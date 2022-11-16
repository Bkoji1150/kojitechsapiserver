from django.urls import path, include
# from .views import movie_list, movie_details
from .views import (ReviewList, CreateReview, PaymentList,
                    StudentsInKojitechs, CoursesInKojitechs,
                   TeacherList,TeacherDetails, PaymentsDetails )

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
courses = DefaultRouter()

router.register(r'students', StudentsInKojitechs, basename='studentsinKojitechs')
courses.register(r'courses', CoursesInKojitechs, basename='coursesinKojitechs')

urlpatterns = [
    path('students/', include(router.urls)),
    path('students/<int:pk>/listpayment/', PaymentList.as_view(), name='paymentdetails'),
    path('students/<int:pk>/makepayment/', PaymentsDetails.as_view(), name='makepayments'),
    path('', include(courses.urls), name="all-courses-list"),
    path("courses/<int:pk>/create-review/", CreateReview.as_view(), name="create-review" ),
    path("courses/<int:pk>/reviews/", ReviewList.as_view(), name="review-list" ),
    #path("reviews/<int:pk>/", CreateView.as_view(), name="review-details" ),
    path("teachers/", TeacherList.as_view(), name="teachers-list" ),
    path("teachers/<int:pk>/", TeacherDetails.as_view(), name="teachers-details"),
] 