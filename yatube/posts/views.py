from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    group_text = 'Группа тайных поклонников графа'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'slug': slug,
        'group': group,
        'posts': posts,
        'group_text': group_text
    }
    return render(request, 'posts/group_list.html', context)
