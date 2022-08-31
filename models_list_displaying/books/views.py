from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    books_list = Book.objects.all().order_by('pub_date')

    context = {'books':books_list }
    return render(request, template, context)


def books_detail(request, pub_date):
    template = 'books/books_detail.html'
    context = {}
    project = ''
    prev = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date')[:1]
    next = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date')[:1]
    try:
            print(prev[0].pub_date)
            print(next[0].pub_date)
    except:
            pass
    current_book = Book.objects.filter(pub_date=pub_date)


    context['books'] = Book.objects.all()
    paginator = Paginator(current_book, 1)
    page = request.GET.get('page')

    try:
        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)
    if prev:
        context['prev'] = prev[0].pub_date
    if next:
        context['next'] = next[0].pub_date
    context['data'] = data

    return  render(request, template, context=context)

