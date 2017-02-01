from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login 
from django.contrib.auth import logout
from django.views import generic
from django.views.generic import View
from django.http import HttpRequest
from django.http import HttpResponseRedirect

from .models import Entry, Post
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def delete_entry(request, post_id, entry_id):
    post = get_object_or_404(Post, pk=post_id)
    entry = Entry.objects.get(pk=entry_id)
    entry.delete()
    return render(request, 'diary/detail.html', {'post': post})

# Create your views here.
class EntryCreate(UpdateView):
	model = Entry
	fields = ['short_text','long_text','photo_url']
	template_name = 'diary/entry_form.html'
	
	def get_queryset(self):
		context_object_name = 'entry_post'
		post = Post.objects.filter(pk=self.kwargs['pk'])
		return post

	def post(self, request, pk):
		e = Entry()
		e.short_text = request.POST.get('short_text')
		e.long_text = request.POST.get('long_text')
		post = get_object_or_404(Post, pk=request.POST.get('post'))

		e.post = post
		e.save()

		return render(request, 'diary/detail.html', {'post': post})

class EntryUpdate(UpdateView):
	model = Entry
	fields = ['short_text','long_text','entry_date']

# Create your views here.
class IndexView(generic.ListView):
	context_object_name = 'all_posts'
	template_name = 'diary/index.html'

	def get_queryset(self):
		return Post.objects.all()

class PostCreate(CreateView):
	model = Post
	fields = ['author', 'title', 'desc', 'created_date','published_date','cover_photo']

class PostDetail(generic.DetailView):
	model = Post
	template_name = 'diary/detail.html'

class PostUpdate(UpdateView):
	model = Post
	fields = ['title', 'desc','cover_photo']