from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.
def home_view(request : HttpResponse):
    posts = Post.objects.all() 
    return render(request, "main/home.html", {"posts": posts})

def create_post_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        new_post = Post(
            title=request.POST["title"],
            content=request.POST["content"],
            is_published="is_published" in request.POST
        )
        new_post.save()

    return render(request, "main/create_post.html")