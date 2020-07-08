from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from fixtures import views

urlpatterns = [
    path('englandfixtures/', views.EnglandFixtureList.as_view()),
    path('japanfixtures/', views.JapanFixtureList.as_view()),
    path('germanfixtures/', views.GermanFixtureList.as_view()),
    path('', views.home, name='home'),
    path('japan/', views.japan, name='japan'),
    path('german/', views.german, name='german'),
    path('england/', views.england, name='england'),
    # path('englandfixtures/<int:pk>/', views.EnglandFixtureDetail.as_view()),
    path('calculategerman/', views.calculategerman, name='calculategerman'),
    path('calculateengland/', views.calculateengland, name='calculateengland'),
    path('calculatejapan/', views.calculatejapan, name='calculatejapan'),
    path('logout', views.logout, name='logout'),
    path('login/', views.login, name='login'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
