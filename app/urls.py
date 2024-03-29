from django.urls import path
from .views import *

urlpatterns = [
    path('', StudentListView.as_view(), name='students'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('student/new/', StudentCreateView.as_view(), name='student_new'),
    path('student/<int:pk>/edit/', StudentUpdateView.as_view(), name='student_edit'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
    path('verify/<int:pk>/', verify, name='verify'),
    path('certificate/<int:pk>/', certificate, name='certificate'),
    path('view_certificate/<int:pk>/', view_cert, name='view_cert'),
]