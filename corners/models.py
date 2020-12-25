from django.db import models


class Country(models.Model):
    name = models.CharField('название страны', max_length=255)
    number = models.IntegerField('номер айди', default=0)

    def __str__(self):
        return self.name


class League(models.Model):
    name = models.CharField('название лиги', max_length=100)
    number = models.IntegerField('номер айди', default=0)
    key = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField('Название тимы', max_length=100)
    number = models.IntegerField('айдишник', default=1)
    key = models.ForeignKey(League, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class StatsCorner(models.Model):
    name = models.CharField('Название тимы', max_length=100)
    home = models.BooleanField("домашний матч")
    away = models.BooleanField("гостевой матч")
    cup = models.BooleanField("кубок")
    league = models.BooleanField("домашняя лига")
    first_half = models.BooleanField("первая половина матча")
    second_half = models.BooleanField("вторая половина матча")
    individual_total = models.DecimalField("ИНДИВИДУАЛЬНЫЙ ТОТАЛ", decimal_places=3, max_digits=4)
    key = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
