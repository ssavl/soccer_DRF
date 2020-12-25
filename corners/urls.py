from django.urls import path
from corners import views


urlpatterns = [
    path('countrys/', views.CountryListView.as_view()),
    path('leagues/', views.LeagueListView.as_view()),
    path('team/', views.TeamListView.as_view()),
]