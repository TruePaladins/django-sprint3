from django.utils import timezone
from django.shortcuts import render, get_object_or_404

from blog.models import Post, Category

POSTS_PER_PAGE=5

def get_objects_filter(category=None):
    query = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True)
    if category is not None:
        query = query.filter(category=category)
    return query

def get_objects_or_404(post_id=None, category_slug=None):
    if post_id is not None:
        variable = get_object_or_404(
            Post,
            id=post_id,
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now()
        )
    elif category_slug is not None:
        variable = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    return variable

def index(request):
    template = 'blog/index.html'
    posts = get_objects_filter()[:POSTS_PER_PAGE]
    context = {'posts': posts}
    return render(request, template, context)

def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_objects_or_404(post_id)
    context = {'post': post}
    return render(request, template, context)

def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_objects_or_404(category_slug)
    posts = get_objects_filter(category=category)
    return render(request, template, {
        'category': category,
        'posts': posts
    })
