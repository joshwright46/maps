from django.urls import path, include
from apps.directory import views
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.CoopList.as_view(), name='coop-list'),
    path('<int:coop_public_id>/', views.CoopDetail.as_view(), name='coop-detail'),
    path('no_coords/', views.CoopsNoCoords.as_view(), name='coop-no-coords'),
    path('unapproved/', views.CoopsUnapproved.as_view(), name='coop-unapproved'),
    path('csv/', views.CoopCSVView.as_view(), name='data'),
    
    path('proposal/', views.CoopProposalList.as_view(), name='coop-proposal-list'),
    path('proposal/<int:pk>/', views.CoopProposalRetrieve.as_view(), name='coop-proposal-detail'),
    path('proposal/create/', views.CoopProposalCreate.as_view(), name='coop-proposal'),
    path('proposal/review/<int:pk>/', views.CoopProposalReview.as_view(), name='coop-review'),

    path('predefined_types/', views.CoopTypeList.as_view()),
    path('types/', views.CoopTypeList.as_view(), name='cooptype-list'),
    path('types/<int:pk>/', views.CoopTypeDetail.as_view(), name='cooptype-detail'),

    path('countries/', views.CountryList.as_view(), name='country-list'),        
    path('states/<str:country_code>', views.StateList.as_view(), name='state-list'),
]