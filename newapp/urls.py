from django.urls import path
from newapp import views



urlpatterns = [
    path("student/", views.StudentAPIView.as_view(), name='student')
]