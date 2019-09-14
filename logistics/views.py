from .models import Post, Material
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import PostCreateForm
from django import forms

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'logistics/home.html', context)


def about(request):
    return render(request, 'logistics/about.html', {'title': 'About'})
    

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'logistics/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ['date']

class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'logistics/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('date')


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MaterialCreateView(LoginRequiredMixin, CreateView):
    model = Material    
    fields = ['name']

    def form_valid(self, form):
        return super().form_valid(form)


class MaterialDetailView(DetailView):
    model = Material



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False