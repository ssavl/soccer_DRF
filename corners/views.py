from django.shortcuts import render
from .models import Country, League, StatsCorner, Team
from rest_framework.views import APIView
from corners.serializers import AllCountry, AllLeague, AllTeam
from rest_framework.response import Response
from rest_framework import status



# Create your views here.


class CountryListView(APIView):
    """вывод списка стран"""

    def get(self, request):
        print(request)
        countrys = Country.objects.filter()
        serializers = AllCountry(countrys, many=True)
        print(serializers)
        return Response(serializers.data)


    def post(self, request):
        serializer = AllCountry(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LeagueListView(APIView):
    """вывод списка лиг"""

    def get(self, request):
        leagues = League.objects.filter()
        serializers = AllLeague(leagues, many=True)
        return Response(serializers.data)


class TeamListView(APIView):
    """вывод списка команд"""

    def get(self, request):
        teams = Team.objects.filter()
        serializers = AllTeam(teams, many=True)
        return Response(serializers.data)


def start(request):
    return render(request, 'index.html')
