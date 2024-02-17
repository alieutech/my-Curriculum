from django.urls import path
from .views import *

urlpatterns = [
    path('curriculums/', CurriculumListCreateAPIView.as_view(), name='curriculum-list-create'),
    path('curriculums/<int:pk>/', CurriculumRetrieveUpdateDestroyAPIView.as_view(), name='curriculum-detail'),
    path('sections/', SectionListCreateAPIView.as_view(), name='section-list-create'),
    path('sections/<int:pk>/', SectionRetrieveUpdateDestroyAPIView.as_view(), name='section-detail'),
]
