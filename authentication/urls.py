from django.urls import path
from .views import SignupView,SigninView

urlpatterns = [
    path('signup/', SignupView.as_view(),name='signup_view'),
    path('signin/', SigninView.as_view(),name='signin_view'),
]