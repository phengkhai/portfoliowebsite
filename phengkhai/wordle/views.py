from django.views import generic
from .models import Post
from django.shortcuts import render,redirect, get_list_or_404, get_object_or_404

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'article_detail.html'
    def post_detail(request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, 'article_detail.html', {'post': post})