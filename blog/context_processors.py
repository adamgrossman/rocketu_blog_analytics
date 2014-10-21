from localflavor.us.us_states import STATES_NORMALIZED
from blog.models import Post, Tag, Ad


def latest_post(request):
    return {
        'latest_post': Post.objects.latest('created')
    }


def all_tags(request):
    return {
        'all_tags': Tag.objects.all(),
        'all_posts': Post.objects.all()
    }


def all_ads(request):
    state = request.location['region'].lower()
    print state
    location = STATES_NORMALIZED[state]
    print location
    random_ad = Ad.objects.filter(state=location).order_by('?')[:1]
    return {
        'all_ads': random_ad,
    }
