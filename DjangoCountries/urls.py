from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('countries-list/page=<int:page>', views.countries_list),
    path('country/<str:name>', views.country_page),
    path('countries/<str:letter>', views.countries_started_from),
    path('languages', views.languages),
    path('language/<str:lang>', views.language)
]
