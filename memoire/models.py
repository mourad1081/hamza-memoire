from django.db import models
from django.utils.timezone import now


class DisplayName:
    def __str__(self):
        if hasattr(self, 'name'):
            return self.name
        if hasattr(self, 'code'):
            return self.code
        if hasattr(self, 'first_name') and hasattr(self, 'last_name'):
            return f'{self.first_name} {self.last_name}'
        if hasattr(self, 'title'):
            return self.title
        if hasattr(self, 'message'):
            return self.message
        return self.id


class Country(DisplayName, models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)


class Affiliation(DisplayName, models.Model):
    name = models.CharField(max_length=300)


class Author(DisplayName, models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    affiliation = models.ForeignKey(Affiliation, null=True, on_delete=models.SET_NULL)
    country = models.ForeignKey(Country, to_field='code', null=True, on_delete=models.SET_NULL)
    email = models.CharField(max_length=100, null=True)


class Journal(DisplayName, models.Model):
    name = models.CharField(max_length=300)


class Discipline(DisplayName, models.Model):
    name = models.CharField(max_length=100)


class Reference(DisplayName, models.Model):
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=500)
    year = models.PositiveIntegerField(null=True)
    journal = models.ForeignKey(Journal, on_delete=models.SET_NULL, null=True)
    volume = models.CharField(max_length=10)
    pages = models.CharField(max_length=20)
    disciplines = models.ManyToManyField(Discipline)


class Comment(DisplayName, models.Model):
    message = models.TextField()
    reference = models.ForeignKey(Reference, on_delete=models.CASCADE)
    created = models.DateTimeField(default=now, null=True)

    class Meta:
        ordering = ('-created',)
