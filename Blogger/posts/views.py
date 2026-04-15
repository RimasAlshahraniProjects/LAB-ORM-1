from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from posts.models import Post

# Create your views here.
def create_post_view(request):
    if request.method == "POST":
        new_post = Post(
            title = request.POST["title"],
            content = request.POST["content"],
            is_published = "is_published" in request.POST,
            poster = request.FILES.get("poster") 
        )
        new_post.save()
        return redirect("main:home_view")
    
    return render(request, "posts/create_post.html")

def post_details_view(request: HttpRequest, post_id: int):
    post = Post.objects.get(pk=post_id)
    
    return render(request, "posts/post_details.html", {"post": post})

def post_update_view(request: HttpRequest, post_id: int):
    post = Post.objects.get(pk=post_id)
    
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.is_published = "is_published" in request.POST
        
        if "poster" in request.FILES:
            post.poster = request.FILES["poster"]
            
        post.save()  
        
        return redirect("posts:post_details_view", post_id=post.id)
    
    return render(request, "posts/post_update.html", {"post": post})


def post_delete_view(request: HttpRequest, post_id: int):
    post = Post.objects.get(pk=post_id)
    post.delete()
    
    return redirect("main:home_view")