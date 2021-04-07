from django.db.models import Value
from django.db.models.functions import Concat
from django.shortcuts import render, get_object_or_404

from memoire.models import Reference, Discipline, Journal, Author, Comment


def home(request):
    return render(request, 'home.html')

def reference(request, reference_id: int):
    ref = get_object_or_404(Reference, pk=reference_id)
    return render(request, 'reference.html', {'reference': ref})

def add_comment(request, reference_id: int):
    ref = get_object_or_404(Reference, pk=reference_id)
    Comment.objects.create(message=request.POST['message'], reference=ref)
    return render(request, 'reference.html', {'reference': ref})


def search(request):
    authors = None
    journals = None
    disciplines = None
    references = None
    total_found = 0
    query = request.GET.get('query', '')

    if request.GET.get('references', False):
        references = Reference.objects.filter(title__icontains=query)
        total_found += references.count()

    if request.GET.get('disciplines', False):
        disciplines = Discipline.objects.filter(name__icontains=query)
        total_found += disciplines.count()

    if request.GET.get('journals', False):
        journals = Journal.objects.filter(name__icontains=query)
        total_found += journals.count()

    if request.GET.get('authors', False):
        name = Concat('first_name', Value(' '), 'last_name')
        authors = Author.objects.annotate(name=name).filter(name__icontains=query)
        total_found += authors.count()

    return render(request, 'results.html', {
        'references': references,
        'authors': authors,
        'disciplines': disciplines,
        'journals': journals,
        'total_found': total_found
    })
