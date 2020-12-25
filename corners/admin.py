from django.contrib import admin

from .models import Country, League, Team, StatsCorner

admin.site.register(Country)
admin.site.register(League)
admin.site.register(Team)
admin.site.register(StatsCorner)
