from django.shortcuts import render
from .models import Post

def render_posts(request):
	posts = Post.objects.all()

	return render(request,'posts.html', {'posts': posts})
