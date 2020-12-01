from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from localmedia.models import Post, Comment,Image
from localmedia.forms import Commentform
from django.views.generic.edit import CreateView
from django.views.generic import ListView,DetailView,TemplateView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from gtts import gTTS 
import os
import playsound
from localmedia.forms import ImageForm
from django.urls import reverse_lazy


def respond(String):
    print(String)
    tts = gTTS(text = String, lang= 'en')
    tts.save("Speech.mp3")
    playsound.playsound("Speech.mp3")
    os.remove("Speech.mp3")

# Create your views here.
@login_required
def index(request):
    q = Post.objects.all()
    return render(request,'index.html',{'q':q})


class PostDetail(LoginRequiredMixin,DetailView):
    model = Post


class PostPost(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['post']
    success_url = '/'

    def form_valid(self, form):
        respond("Your post is successfully shared")
        form.instance.user = self.request.user
        return super().form_valid(form)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            respond("Account successfully created.")
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('localmedia:index')
    else:
        respond("Now you are going to create a new account. Please follow the instructions")
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

class ImagePost(request,pk):
    form = ImageForm
    template_name = 'imageform.html'
    q = get_object_or_404(Post,pk = pk)
    if request.method == 'POST':
        form = ImageForm(request.FILES)
        if form.is_valid():
            image = form.save(commit = False)
            image.post = q
            image.user = request.user
            image.save()
            return redirect('localmedia:detail', pk = q.pk)
    else:
            form = ImageForm()
            return render(request,'localmedia/imageform.html',{'form':form})

    
  
  

@login_required
def add_comment_to_post(request,pk):
    q = get_object_or_404(Post,pk = pk)
    if request.method =='POST':
        form = Commentform(request.POST)
        if form.is_valid():
            respond("Your comment is successfully posted")
            comment = form.save(commit = False)
            comment.post = q
            comment.user = request.user
            comment.save()
            return redirect('localmedia:detail', pk = q.pk)
    else:
        respond("You are going to add a comment to that post")
        form = Commentform()
    return render(request,'localmedia/comment_form.html',{'form':form})

class ImageDisplay(DetailView):
    model = Image
    template_name = 'post_detail.html'
    context_object_name = 'localmedia'

@login_required
def logout_view(request):
    respond("Logging out. See you soon")
    logout(request)
    return redirect('localmedia:index')

