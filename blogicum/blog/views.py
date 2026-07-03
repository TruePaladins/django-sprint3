from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post

POSTS_PER_PAGE = 5


def get_posts():
    return Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )


def index(request):
    template = 'blog/index.html'
    posts = get_posts()[:POSTS_PER_PAGE]
    context = {'posts': posts}
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post,
        id=post_id,
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    posts = get_posts().filter(category=category)
    return render(request, template, {
        'category': category,
        'posts': posts,
    })
