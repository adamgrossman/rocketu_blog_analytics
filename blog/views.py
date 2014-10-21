from django.shortcuts import render, get_object_or_404
from blog.models import Post, Tag


def blog(request):
    return render(request, 'blog.html', {
        'posts': Post.objects.order_by('-created'),
    })


def post(request, pk):
    post_obj = get_object_or_404(Post, pk=pk)

    return render(request, 'post.html', {
        'post': post_obj
    })


def tag(request, tag_id):
    tags = Tag.objects.get(pk=tag_id)
    data = {'tags': tags}
    return render(request, 'tags.html', data)
