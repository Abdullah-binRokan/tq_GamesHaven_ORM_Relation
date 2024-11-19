from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Game, Review, Category
from .forms import GameForm

# Create your views here.

def create_game_view(request:HttpRequest):

    game_form = GameForm()

    # define categories so we can pass it as context
    categories = Category.objects.all()

    if request.method == "POST":
        # game_form = GameForm(request.POST, request.FILES)
        # if game_form.is_valid():
        #     game_form.save()
        #     return redirect('main:home_view')
        # else:
        #     print("not valid form", game_form.errors)

        new_game = Game(title=request.POST["title"], description=request.POST["description"], publisher=request.POST["publisher"], rating=request.POST["rating"], release_date=request.POST["release_date"], poster=request.FILES["poster"])
        new_game.save()
        # use set to add categories (many to many field) to the new_game object
        new_game.categories.set(request.POST.getlist("categories"))

        return redirect('main:home_view')
    

    return render(request, "games/create.html", {"game_form":game_form,"RatingChoices": reversed(Game.RatingChoices.choices), "categories": categories})


def game_detail_view(request:HttpRequest, game_id:int):

    game = Game.objects.get(pk=game_id)

    reviews = Review.objects.filter(game=game)

    return render(request, 'games/game_detail.html', {"game" : game, "reviews": reviews})


def game_update_view(request:HttpRequest, game_id:int):

    game = Game.objects.get(pk=game_id)

    if request.method == "POST":
        game.title = request.POST["title"]
        game.description = request.POST["description"]
        game.release_date = request.POST["release_date"]
        game.publisher = request.POST["publisher"]
        game.rating = request.POST["rating"]
        if "poster" in request.FILES: game.poster = request.FILES["poster"]
        game.save()



        return redirect("games:game_detail_view", game_id=game.id)

    return render(request, "games/game_update.html", {"game":game})


def game_delete_view(request:HttpRequest, game_id:int):

    game = Game.objects.get(pk=game_id)
    game.delete()

    return redirect("main:home_view")


def all_games_view(request:HttpRequest):
    #games = Game.objects.filter(rating__gte=3).order_by("-release_date")
    #games = Game.objects.filter(rating__gte=3).exclude(title__contains="Legends").order_by("-release_date")
    games = Game.objects.all().order_by("-release_date")

    #results count
    print(games.count())

    return render(request, "games/all_games.html", {"games":games})


def search_games_view(request:HttpRequest):

    if "search" in request.GET and len(request.GET["search"]) >= 3:
        games = Game.objects.filter(title__contains=request.GET["search"])

        if "order_by" in request.GET and request.GET["order_by"] == "rating":
            games = games.order_by("-rating")
        elif "order_by" in request.GET and request.GET["order_by"] == "release_date":
            games = games.order_by("-release_date")
    else:
        games = []


    return render(request, "games/search_games.html", {"games" : games})

def add_review_view(request: HttpRequest, game_id: int):
    if request.method == "POST":
        game_object = Game.objects.get(pk=game_id)
        new_review = Review(game=game_object, name=request.POST["name"], comment=request.POST["comment"], rating=request.POST["rating"])
        new_review.save()

    return redirect("games:game_detail_view", game_id=game_id)