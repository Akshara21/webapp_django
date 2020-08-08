from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Posts


# from django.contrib.messages.views import SuccessMessageMixin

def home(request):
    context = {
        'posts' : Posts.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostsListView(ListView):
    model = Posts
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 5

class UserPostsListView(ListView):
    model = Posts
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Posts.objects.filter(name=user).order_by('-date')


class PostsDetailView(DetailView):
    model = Posts

class PostsCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    fields = ['title', 'content']

    def form_valid(self, form):
        # form validity check if the name given matches with that of the user with which we signed in
        # we can do the form validity check then
        form.instance.name = self.request.user
        # if the name is matched then we can validate form by passing form valid method with that of super class method
        # also we need to pass the form within the form valid
        return super().form_valid(form)

class PostsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # this test_func is used to run UserPassesTestMixin which is to give access to the owner user to alone access the profile and to update changes
        post = self.get_object()
        # to get the post that we are trin to update
        if self.request.user == post.name:
            return True
        return False

class PostsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Posts
    success_url = '/blog/home/'
# success_url s only required for delete view for update and create get_absolute_url to redirect to the page (shud be given in models.py)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.name:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})

def latest(request):
    return render(request,'blog/latest.html')
