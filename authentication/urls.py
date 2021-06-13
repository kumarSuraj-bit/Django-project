from django.urls import path
from .views import SignupView,SigninView,SignoutView
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView,
    )

urlpatterns = [
    path('signup/', SignupView.as_view(),name='signup_view'),
    path('signin/', SigninView.as_view(),name='signin_view'),
    path('signout/', SignoutView.as_view(),name='signout_view'),

    path('password/reset/',PasswordResetView.as_view(),name='password_reset'),
    path('password/reset/done/',PasswordResetDoneView.as_view() ,name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>',PasswordResetConfirmView.as_view() ,name='password_reset_confirm'),
    path('password/reset/complete/',PasswordResetCompleteView.as_view() ,name='password_reset_complete'),
]