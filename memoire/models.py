from django.db import models
from django.utils.timezone import now


class Country(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)


class Affiliation(models.Model):
    name = models.CharField(max_length=300)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    affiliation = models.ForeignKey(Affiliation, null=True, on_delete=models.SET_NULL)
    country = models.ForeignKey(Country, to_field='code', null=True, on_delete=models.SET_NULL)
    email = models.CharField(max_length=100, null=True)


class Journal(models.Model):
    name = models.CharField(max_length=300)


class Discipline(models.Model):
    name = models.CharField(max_length=100)


class Reference(models.Model):
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=500)
    year = models.PositiveIntegerField(null=True)
    journal = models.ForeignKey(Journal, on_delete=models.SET_NULL, null=True)
    volume = models.CharField(max_length=10)
    pages = models.CharField(max_length=20)
    disciplines = models.ManyToManyField(Discipline)


class Comment(models.Model):
    message = models.TextField()
    reference = models.ForeignKey(Reference, on_delete=models.CASCADE)
    created = models.DateTimeField(default=now, null=True)

    class Meta:
        ordering = ('-created',)
