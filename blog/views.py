from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from .forms import NewPostForm
from django.shortcuts import redirect

def posts_list_view(request):
    
    posts = Post.objects.filter(published=True).order_by('-updated_at')
    return render(request, 'blog/posts_list.html', context={'posts' : posts})


def post_detail_view(request,pk):

    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', context={'post' : post})

def create_post_view(request):
    if request.method == "POST":
      form = NewPostForm(request.POST)
      if form.is_valid() : 
         form.save()
         form = NewPostForm()
         return redirect('posts_list')

    else : 
      form = NewPostForm()

    return render(request, 'blog/add_post.html', context={'form' : form})


def update_post_view(request, pk):
   
   post = get_object_or_404(Post, pk=pk)
   form = NewPostForm(request.POST or None, instance=post)

   if form.is_valid():
      form.save()
      return redirect('post_detail', pk)

   return render(request, 'blog/add_post.html', context={'form': form})

def delete_post(request, pk):
   
   post = get_object_or_404(Post, pk=pk)
   if request.method == "POST":
      post.delete()
      return redirect('posts_list')
   return render(request, 'blog/post_delete.html', context={'post':post})


   
