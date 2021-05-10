from django.db.models import Value
from django.db.models.functions import Concat
from django.shortcuts import render, get_object_or_404, redirect

from memoire.models import Reference, Discipline, Journal, Author, Comment


def home(request):
    return render(request, 'home.html')


def reference(request, reference_id: int):
    ref = get_object_or_404(Reference, pk=reference_id)
    ref.seen += 1
    ref.save()
    # similar_references = Reference.objects.filter(disciplines__in=ref.disciplines.all())
    similar_references = Reference.objects.all()[:10]
    return render(request, 'reference.html', {
        'reference': ref,
        'similar_references': similar_references
    })


def journal(request, journal_id: int):
    j = get_object_or_404(Journal, pk=journal_id)
    return render(request, 'journal.html', {'journal': j})


def author(request, author_id: int):
    a = get_object_or_404(Author, pk=author_id)
    return render(request, 'author.html', {'author': a})


def discipline(request, discipline_id: int):
    d = get_object_or_404(Discipline, pk=discipline_id)
    return render(request, 'discipline.html', {'discipline': d})


def add_comment(request, reference_id: int):
    ref = get_object_or_404(Reference, pk=reference_id)
    Comment.objects.create(message=request.POST['message'], reference=ref)
    return redirect('reference', reference_id=ref.id)


def search(request):
    query = request.GET.get('query', '')
    models = {
        'references': {'model': Reference, 'filters': {'title__icontains': query}},
        'disciplines': {'model': Discipline, 'filters': {'name__icontains': query}},
        'journals': {'model': Journal, 'filters': {'name__icontains': query}},
        'authors': {'model': Author, 'filters': {}},
        'years': {'model': Reference, 'filters': {'year': query}},
    }
    model = models[request.GET.get('type', 'references')]['model']
    filters = models[request.GET.get('type', 'references')]['filters']
    items = model.objects.filter(**filters)

    # custom author name field
    if request.GET.get('type', 'references') == 'authors':
        name = Concat('first_name', Value(' '), 'last_name')
        items = items.annotate(name=name).filter(name__icontains=query)

    return render(request, 'results.html', {
        'results': items,
        'type': request.GET.get('type', 'references')
    })
