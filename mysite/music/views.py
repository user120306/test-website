from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from models import Album, Song
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .forms import UserForm
from django.http import HttpRequest
from django.http import HttpResponseRedirect

AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

# Create your views here.
@login_required(login_url="/music/login_user/")

def restricted(request):
    return HttpResponse('Rango says: since you are an authenticated user you can view this restricted page.')

class AlbumCreate(LoginRequiredMixin, CreateView):
	login_url="/music/login_user/"
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(LoginRequiredMixin, DeleteView):
	login_url="/music/login_user/"
	model = Album
	success_url = reverse_lazy('music:index')

class AlbumUpdate(LoginRequiredMixin, UpdateView):
	login_url="/music/login_user/"
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']

class DetailView(LoginRequiredMixin, generic.DetailView):
	login_url="/music/login_user/"
	model = Album
	template_name = 'music/detail.html'

def delete_song(request, album_id, song_id):
    album = get_object_or_404(Album, pk=album_id)
    song = Song.objects.get(pk=song_id)
    song.delete()
    return render(request, 'music/detail.html', {'album': album})

def favourite_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if album.is_favourite:
    	album.is_favourite = False
    else:
    	album.is_favourite = True
    album.save()
    return redirect('music:index')

def favourite_song(request, song_id):
    song = Song.objects.get(pk=song_id)
    album = get_object_or_404(Album, pk=song.album.pk)
    url = request.META.get('HTTP_REFERER')

    if song.is_favourite:
    	song.is_favourite = False
    else:
    	song.is_favourite = True
    song.save()

    return HttpResponseRedirect(url)

#@login_required(login_url="/music/login_user/")
class IndexView(generic.ListView):
    context_object_name = 'all_albums'
    template_name = 'music/index.html'

    def get_queryset(self):
        #albums = Album.objects.filter(user=self.request.user)
        albums = Album.objects.all()
        song_results = Song.objects.all()
        query = self.request.GET.get("q")
        
        if query:
            albums = albums.filter(
                Q(album_title__icontains=query) |
                Q(artist__icontains=query)
           ).distinct()
        #    song_results = song_results.filter(
        #        Q(song_title__icontains=query)
        #    ).distinct()
            return render(self.request, 'music/index.html', {
                'all_albums': albums,
                'songs': song_results
	        })

        return {'all_albums': albums}

    def get_context_data(self, **kwargs):
	    context = super(RandomNumberView, self).get_context_data(**kwargs)
	    context['number'] = random.randrange(1, 100)
	    return context

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
}
    return render(request, 'music/login.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'albums': albums})
            else:
                return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/login.html', {'error_message': 'Invalid login'})
    return render(request, 'music/login.html')

class SongCreate(LoginRequiredMixin, UpdateView):
	login_url="/music/login_user/"
	#context_object_name = 'all_albums'
	template_name = 'music/song_form.html'
	model = Song
	fields = ['song_title', 'audio_file']
	
	def get_queryset(self):
		context_object_name = 'album'
		album = Album.objects.filter(pk=self.kwargs['pk'])
		return album

	def post(self, request, pk):
		m = Song()
		m.song_title = request.POST.get('song_title')
		m.file_type = request.POST.get('file_type')
		album = get_object_or_404(Album, pk=request.POST.get('album'))

		m.album = album
		m.save()
		url = request.META.get('HTTP_REFERER')

		return HttpResponseRedirect(url)

class SongView(LoginRequiredMixin, generic.ListView):
	login_url="/music/login_user/"
	context_object_name = 'song_list'
	template_name = 'music/song.html'

	def get_queryset(self):
		return Song.objects.all()

class UserFormView(View):
	form_class = UserForm
	template_name = 'music/registration_form.html'

	#display lank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form':form})

	#process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)
			
			#clean (normalise) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			#return user object if credentials are correct
			user = authenticate(username=username, password=password)

			if user is not None:

				if user.is_active:
					login(request, user)
					return redirect('music:index')
		return render(request, self.template_name, {'form':form})
