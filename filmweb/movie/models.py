from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=32, verbose_name = "Imie")
    last_name = models.CharField(max_length=32, verbose_name = "Nazwisko")

class Genre(models.Model):
    name = models.CharField(max_length=32, verbose_name="Gatunek")

class Movie(models.Model):
    title = models.CharField(max_length=128, verbose_name="Tytul")
    director = models.ForeignKey(Person, related_name="director", verbose_name="Rezyser", on_delete=models.SET_NULL, null=True)
    screenplay = models.ForeignKey(Person, related_name="screenplay", verbose_name="Scenariusz", on_delete=models.SET_NULL, null=True)
    starring = models.ManyToManyField(Person, through='PersonMovie',  verbose_name="Aktorzy")
    year = models.IntegerField(verbose_name="Rok produkcji")
    rating = models.FloatField(verbose_name="Ocena filmu")
    genre = models.ManyToManyField(Genre, verbose_name="Gatunek")

class PersonMovie(models.Model):
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    movie = models.ForeignKey(Movie,on_delete=models.SET_NULL, null=True)
    role = models.CharField(max_length=128)