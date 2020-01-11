from django.shortcuts import render, redirect
from .models import Game
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

def game_list(request):
    games = Game.objects.all().order_by('title')
    return render(request, "games/game_list.html", {'games':games})


def game_detail(request, slug):
    #return HttpResponse("slug: " +slug)
    game = Game.objects.get(slug=slug)
    return render(request, "games/game_detail.html", {'game':game} )

@login_required(login_url="/accounts/login")
def upload_game(request):
    if request.method=="POST":
        form = forms.UploadGame(request.POST, request.FILES)
        if form.is_valid():
            #save game to database
            instance = form.save(commit=False)
            instance.developer = request.user
            instance.save()
            return redirect('games:list')
    else:
        form = forms.UploadGame()
    return render(request, 'games/upload_game.html', {"form":form})