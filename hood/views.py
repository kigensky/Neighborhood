from django.shortcuts import render

# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView,)
from .models import Post,Hood
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

    # def get_queryset(self):
    #     return Post.objects.filter(hood=self.request.user.profile.hood)