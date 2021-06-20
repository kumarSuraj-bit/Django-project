from django.urls import path
from .views import ProfileView,ProfileeditView

urlpatterns = [
    path('in/<str:username>/',ProfileView.as_view(),name='Profile_view'),
    path('in/<str:username>/edit/',ProfileeditView.as_view(),name='Profile_edit_view'),
]