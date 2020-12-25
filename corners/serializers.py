from .models import Country, StatsCorner, League, Team
from rest_framework import serializers


class AllLeague(serializers.ModelSerializer):

    class Meta:
        model = League
        fields = '__all__'


class AllCountry(serializers.ModelSerializer):
    league_set = AllLeague(many=True, read_only=True)

    class Meta:
        model = Country
        fields = '__all__'



class AllTeam(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'  # Сюда вводить поля для вывода в api





