from analytics.models import Page


def location(request):
    return {
        'location': request.location
    }


def all_pages(request):
    return {
        'all_pages': Page.objects.all(),
    }
