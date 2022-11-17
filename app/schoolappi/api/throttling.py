from rest_framework.throttling import UserRateThrottle


class ReviewCreateThrottle(UserRateThrottle):
    scope = 'review-create'


class ReviewDeleteThrottle(UserRateThrottle):
    scope ='review-list'
