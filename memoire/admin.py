from django.contrib import admin
# the module name is app_name.models
# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
from memoire.models import Reference, Author, Country, Affiliation, Discipline, Journal, Comment

admin.site.register(Author)
admin.site.register(Country)
admin.site.register(Affiliation)
admin.site.register(Reference)
admin.site.register(Journal)
admin.site.register(Comment)
admin.site.register(Discipline)
