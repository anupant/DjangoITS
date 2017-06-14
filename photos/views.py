
from .models import Album,Song
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
#redirect page will redirect you from whatever u want
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .models import Album
from .forms import UserForm
# Create your views here.


'''
#separating your database from a django logic

# we named it index , because we named index in photos/urls.py
#we are trying to print list of albums on this page
def index(request):
    all_albums = Album.objects.all()
    #template = loader.get_template("photos/index.html")
    #essentially information your template needs
    #context = {'all_albums':all_albums}
    #return render(request,'photos/index.html',context)
    return render(request,'photos/index.html',{'all_albums':all_albums})

#Present detail only after checking that album_id is present
def detail(request , album_id):
    album = get_object_or_404(Album , pk = album_id)
    return render(request,'photos/detail.html',{'album': album})

def favorite(request,album_id):
    album = get_object_or_404(Album ,pk = album_id)
    try:
        selected_song = album.song_set.get(pk = request.POST['song'])
    except(KeyError,Song.DoesNotExist):
        return render(request,'photos/detail.html',{
            'album': album,
             'error_message': "You did not select a valid song",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request,'photos/detail.html',{'album': album})

'''

class IndexView(generic.ListView):
    template_name = 'photos/index.html'
    context_object_name = 'all_albums'
    #By default the list of all objects is returned by object_list
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'photos/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('photos:index')

#Inheriting from view Class based views
class UserFormView(View):
    form_class = UserForm
    template_name = 'photos/registration_form.html'

    # display blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name ,{'form':form})

    # process form data
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            #At this point the data is not commited in the database
            user = form.save(commit = False)

            #cleaned(normalized) data which can be plopped in the database
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)

            user.save()

            user = authenticate(username = username , password = password)

            if user is not None:

                if user.is_active:
                    #logging in to the user
                    login(request,user)
                    return redirect('photos:index')

        #if not properly authenticated , here it is a blank url
        return render(request,self.template_name ,{'form':form})




