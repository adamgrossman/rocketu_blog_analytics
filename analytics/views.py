from django.shortcuts import render
from analytics.models import Page


def main(request):
    return render(request, 'main.html')


def view_page(request, page_id):
    page = Page.objects.get(pk=page_id)
    data = {"page": page}
    return render(request, 'view.html', data)
