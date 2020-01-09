from django.shortcuts import render
from .models import Game
from django.http import HttpResponse
def game_list(request):
    games = Game.objects.all().order_by('title')
    return render(request, "games/game_list.html", {'games':games})


def game_detail(request, slug):
    #return HttpResponse("slug: " +slug)
    game = Game.objects.get(slug=slug)
    return render(request, "games/game_detail.html", {'game':game} )