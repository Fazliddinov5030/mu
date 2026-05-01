from django.shortcuts import render, get_object_or_404
from .models import Category, Post

# Create your views here.


def home_page(request):
    """Home page displaying all posts with category sidebar"""
    category_filter = request.GET.get('category')
    
    if category_filter:
        posts = Post.objects.filter(category__slug=category_filter)
    else:
        posts = Post.objects.all()
    
    categories = Category.objects.all()
    featured_posts = Post.objects.filter(is_featured=True)[:3]
    
    context = {
        'posts': posts,
        'categories': categories,
        'featured_posts': featured_posts,
        'current_category': category_filter,
    }
    return render(request, 'project2/index.html', context)


def post_detail(request, slug):
    """Detail page for a single post"""
    post = get_object_or_404(Post, slug=slug)
    categories = Category.objects.all()
    
    # Get related posts from same category
    related_posts = Post.objects.filter(
        category=post.category
    ).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'categories': categories,
        'related_posts': related_posts,
    }
    return render(request, 'project2/detail.html', context)