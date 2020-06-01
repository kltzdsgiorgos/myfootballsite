from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from fixtures import views

urlpatterns = [
    path('fixtures/', views.FixtureList.as_view()),
    path('fixtures/<int:pk>/', views.FixtureDetail.as_view()),
    path('', views.index, name='index'),
    path('calculate/', views.calculate, name='calculate')
]

urlpatterns = format_suffix_patterns(urlpatterns)