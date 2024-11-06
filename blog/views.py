from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from .forms import NewPostForm
from django.shortcuts import redirect
from django.views import generic
from django.urls import reverse_lazy


class PostListView(generic.ListView):

   template_name = 'blog/posts_list.html'
   context_object_name = 'posts'

   def get_queryset(self):
      return Post.objects.filter(published=True).order_by('-updated_at')

# def posts_list_view(request):
    
#     posts = Post.objects.filter(published=True).order_by('-updated_at')
#     return render(request, 'blog/posts_list.html', context={'posts' : posts})

class PostDetailView(generic.DetailView):

   model = Post
   template_name = 'blog/post_detail.html'
   context_object_name = 'post'

# def post_detail_view(request,pk):

#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', context={'post' : post})

class PostCreateView(generic.CreateView):

   form_class = NewPostForm
   template_name = 'blog/add_post.html'

# def create_post_view(request):
#     if request.method == "POST":
#       form = NewPostForm(request.POST)
#       if form.is_valid() : 
#          form.save()
#          form = NewPostForm()
#          return redirect('posts_list')

#     else : 
#       form = NewPostForm()

#     return render(request, 'blog/add_post.html', context={'form' : form})

   
class PostUpdateView(generic.UpdateView):

   model = Post
   form_class = NewPostForm
   template_name = 'blog/add_post.html'

# def update_post_view(request, pk):
#    post = get_object_or_404(Post, pk=pk)
#    form = NewPostForm(request.POST or None, instance=post)
#    if form.is_valid():
#       form.save()
#       return redirect('post_detail', pk)
#    return render(request, 'blog/add_post.html', context={'form': form})

class PostDeleteView(generic.DeleteView):

   model = Post
   template_name = 'blog/post_delete.html'
   success_url = reverse_lazy('posts_list')
   
# def delete_post(request, pk):
#    post = get_object_or_404(Post, pk=pk)
#    if request.method == "POST":
#       post.delete()
#       return redirect('posts_list')
#    return render(request, 'blog/post_delete.html', context={'post':post})


   
