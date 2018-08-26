from django.shortcuts import render, redirect
#from django.views.generic import ListView
from .models import Blog
from .forms import BlogForm


#class HomePageView(ListView):
#    model = Blog
#    template_name = 'home.html'

def list_blogs(request):
	blogs = Blog.objects.all()
	return render(request,'blogs.html',{'blogs':blogs})

def create_blog(request):
	form = BlogForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('list_blogs')

	return render(request,'blog-form.html',{'form':form})

def update_blog(request, id):
	blog = Blog.objects.get(id= id)
	form = BlogForm(request.POST or None, instance=blog)
	

	if form.is_valid():
		form.save()
		return redirect('list_blogs')

	return render(request,'blog-form.html',{'form':form,'blog':blog})

def delete_blog(request, id):
	blog = Blog.objects.get(id= id)

	if request.method == 'POST':
		blog.delete()
		return redirect('list_blogs')

	return render(request,'blog-delete-confirm.html',{'blog':blog})				