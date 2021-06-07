from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
# from .models import Post,Mtaa
from .models import Post, Business, Essential, Mtaa
from django.urls import reverse_lazy
from .forms import PostCreateForm
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(title__icontains=query)
        else:
            return Post.objects.all()
        
class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    success_url = reverse_lazy('hood-home')
    fields = ['title', 'body', 'cloudinary_image','creator', 'Mtaa']
    success_message = "The Post created successfully!"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        # form.instance.mtaa = self.request.user.profile.mtaa
        return super(PostCreateView, self).form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.creator:
            return True
        return False        
        
class PostUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    success_url = reverse_lazy('hood-home')
    fields = ['title', 'body', 'cloudinary_image']
    success_message = "The Post updated successfully!"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.mtaa = self.request.user.profile.mtaa
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.creator:
            return True
        return False


class PostDetailView(DetailView):
    model = Post
    success_url = reverse_lazy('hood-home')


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('hood-home')
    success_message = "The Post %(title) was deleted successfully!"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.creator:
            return True
        return False


class BusinessListView(ListView):
    model = Business
    template_name = 'business_list.html'
    queryset = Business.objects.order_by('-timestamp')

    # def get_queryset(self):
    #     return Business.objects.filter(mtaa=self.request.user.profile.mtaa)
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(title__icontains=query)
        else:
            return Post.objects.all()  

class BusinessCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Business
    success_url = reverse_lazy('business-home')
    fields = ['title', 'email', 'body', 'cloudinary_image']
    success_message = "Business created successfully!"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.mtaa = self.request.user.profile.mtaa
        return super().form_valid(form)

    def test_func(self):
        business = self.get_object()
        if self.request.user == business.owner:
            return True
        return False


class BusinessUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Business
    success_url = reverse_lazy('business-home')
    fields = ['title', 'email', 'body', 'cloudinary_image']
    success_message = "The Business updated successfully!"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.mtaa = self.request.user.profile.mtaa
        return super().form_valid(form)

    def test_func(self):
        business = self.get_object()
        if self.request.user == business.owner:
            return True
        return False


class BusinessDetailView(DetailView):
    model = Business
    success_url = reverse_lazy('business-home')


class BusinessDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Business
    success_url = reverse_lazy('business-home')
    success_message = "The Business %(title) was deleted successfully!"

    def test_func(self):
        business = self.get_object()
        if self.request.user == business.owner:
            return True
        return False


class EssentialListView(ListView):
    model = Essential
    template_name = 'essential_list.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(title__icontains=query)
        else:
            return Post.objects.all() 

    # def get_queryset(self):
    #     return Essential.objects.filter(mtaa=self.request.user.profile.mtaa).order_by('title')


class EssentialCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Essential
    success_url = reverse_lazy('essential-home')
    fields = ['title', 'officer', 'phone', 'email', 'mtaa', 'cloudinary_image']
    success_message = "Essential created successfully!"


class EssentialUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Essential
    success_url = reverse_lazy('essential-home')
    fields = ['title', 'officer', 'phone', 'email', 'mtaa', 'cloudinary_image']
    success_message = "The Essential updated successfully!"


class EssentialDetailView(DetailView):
    model = Essential
    success_url = reverse_lazy('essential-home')


class EssentialDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Essential
    success_url = reverse_lazy('essential-home')
    success_message = "The Essential %(title) was deleted successfully!"


class MtaaListView(ListView):
    model = Mtaa
    template_name = 'mtaa_list.html'
    queryset = Mtaa.objects.order_by('title')

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Mtaa.objects.filter(title__icontaihoodns=query)
        else:
            return Mtaa.objects.order_by('title')


class MtaaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Mtaa
    success_url = reverse_lazy('mtaa-home')
    fields = ['title', 'location', 'admin', 'cloudinary_image']
    success_message = "Mtaa was created successfully!"


class MtaaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Mtaa
    success_url = reverse_lazy('mtaa-home')
    fields = ['title', 'location', 'admin', 'cloudinary_image']
    success_message = "Your Mtaa has been updated successfully!"


class MtaaDetailView(DetailView):
    model = Mtaa
    success_url = reverse_lazy('mtaa-home')


class MtaaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mtaa
    success_url = reverse_lazy('mtaa-home')
    success_message = "Your Mtaa %(title) was deleted successfully!"        