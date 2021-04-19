# Generated by Django 3.1.7 on 2021-04-19 16:57
import numpy as np
import pandas
from django.db import migrations


def add_data(apps, schema_editor):
    Affiliation = apps.get_model('memoire', 'Affiliation')
    Author = apps.get_model('memoire', 'Author')
    Country = apps.get_model('memoire', 'Country')
    Journal = apps.get_model('memoire', 'Journal')
    Reference = apps.get_model('memoire', 'Reference')

    data_frames = pandas.read_excel('memoire/migrations/promethee.xlsx', sheet_name=None, engine='openpyxl')
    authors = data_frames['Authors'].replace({np.nan: None})
    authors = [{
        'first_name': fn or 'N/A',
        'last_name': ln or 'N/A',
        'affiliation': aff or 'N/A',
        'country': country or 'N/A',
        'email': email or 'N/A'
    } for fn, ln, aff, country, email in zip(
        authors['1st name'],
        authors['Last name'],
        authors['Affiliation'],
        authors['Country'],
        authors['Email']
    )]

    for author in authors:
        affiliation, _ = Affiliation.objects.get_or_create(name=author['affiliation'])
        country, _ = Country.objects.get_or_create(code=author['country'])
        try:
            Author.objects.get_or_create(**{**author, 'affiliation': affiliation, 'country': country})
        except Author.MultipleObjectsReturned:
            pass

    print('Authors finished...')
    references = data_frames['BiblioPromethee'].replace({np.nan: None})
    references = [{
        'title': title or 'N/A',
        'year': year or None,
        'journal': journal or 'N/A',
        'pages': pages or 'N/A',
        'volume': volume or 'N/A',
        'authors': _authors or 'N/A'
    } for title, year, journal, pages, volume, _authors in zip(
        references['Title'],
        references['Year'],
        references['Journal or book'],
        references['Pages'],
        references['Volume'],
        references['Authors']
    )]

    for reference in references:
        journal, _ = Journal.objects.get_or_create(name=reference['journal'])
        authors = reference['authors'].split('.,')
        del reference['authors']
        ref, _ = Reference.objects.get_or_create(**{**reference, 'journal': journal})
        no_affiliation = Affiliation.objects.get(name='N/A')
        no_country = Country.objects.get(code='N/A')
        for author in authors:
            try:
                first_name, last_name = author.split(',')
                _as = Author.objects.filter(first_name=first_name, last_name__iexact=last_name.replace('.', ''))
                if _as.exists():
                    _a = _as.first()
                else:
                    _a = Author.objects.create(**{
                        'first_name': first_name or 'N/A',
                        'last_name': last_name or 'N/A',
                        'affiliation': no_affiliation,
                        'country': no_country,
                        'email': 'N/A'
                    })
                ref.authors.add(_a)
            except ValueError:
                print('ERROR:', author)

    print('references finished!')


class Migration(migrations.Migration):
    dependencies = [
        ('memoire', '0003_auto_20210407_1733'),
    ]

    operations = [
        migrations.RunPython(add_data, migrations.RunPython.noop),
    ]
