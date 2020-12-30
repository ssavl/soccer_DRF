from django.shortcuts import render
from .models import Country, League, StatsCorner, Team
from rest_framework.views import APIView
from corners.serializers import AllCountry, AllLeague, AllTeam, AllStatistic
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework import mixins


# Create your views here.


class CountryListView(APIView):
    """вывод списка стран"""

    def get(self, request):
        print(f"request::: {request}")
        countrys = Country.objects.filter()
        serializers = AllCountry(countrys, many=True)
        print(f"serializers::: {serializers}")
        return Response(serializers.data)

    def post(self, request):
        serializer = AllCountry(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# class LeagueListView(APIView):
#     """вывод списка лиг"""
#
#     def get(self, request):
#         leagues = League.objects.filter()
#         serializers = AllLeague(leagues, many=True)
#         return Response(serializers.data)


class TeamListView(APIView):
    """вывод списка команд"""

    def get(self, request):
        teams = Team.objects.filter()
        serializers = AllTeam(teams, many=True)
        return Response(serializers.data)

# ------------------------------------CLASS-BASED---------------------------------------------------

class StatisticListView(APIView):
    "вывод списка статистических данных"

    def get(self, request):
        stats = StatsCorner.objects.filter()
        serializers = AllStatistic(stats, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializer = StatisticListView(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class StatisticDetail(APIView):
    """
    Детальная информация по одному элементу
    """

    def get_object(self, pk):
        try:
            stat = StatsCorner.objects.get(pk=pk)
            print('qweqwe', stat)
            return stat
        except StatsCorner.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = AllStatistic(snippet)
        return Response(serializer.data)


class CountryDetail(APIView):
    """
    Детальная информация по одному элементу Страны
    """

    def get_object(self, pk):
        try:
            stat = Country.objects.get(pk=pk)
            print('qweqwe', stat)
            return stat
        except Country.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = AllCountry(snippet)
        return Response(serializer.data)

# ------------------------------------GENERIC------------------------------------------


class LeagueList(generics.ListCreateAPIView):
    queryset = League.objects.all()
    serializer_class = AllLeague


class LeagueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = League.objects.all()
    serializer_class = AllLeague


def start(request):
    return render(request, 'index.html')


# ---------------------------------------MIXIN------------------------------------


class TeamList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Team.objects.all()
    serializer_class = AllTeam

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class TeamDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Team.objects.all()
    serializer_class = AllTeam

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)