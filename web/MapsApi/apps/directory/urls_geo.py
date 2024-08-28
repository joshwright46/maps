from django.urls import path
from apps.directory import views

urlpatterns = [
    path('countries/', views.CountryList.as_view(), name='country-list'),        
    path('states/<str:country_code>', views.StateList.as_view(), name='state-list'),
]