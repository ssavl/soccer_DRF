from django.urls import path
from corners import views
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('countrys/', views.CountryListView.as_view()),
    path('leagues/', views.LeagueList.as_view()),
    path('leagues/<int:pk>', views.LeagueDetail.as_view()),
    path('team/', views.TeamList.as_view()),
    path('team/<int:pk>', views.TeamDetail.as_view()),
    path('statistic/', views.StatisticListView.as_view()),
    path('statistic/<int:pk>', views.StatisticDetail.as_view()),
    path('countrys/<int:pk>', views.CountryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
