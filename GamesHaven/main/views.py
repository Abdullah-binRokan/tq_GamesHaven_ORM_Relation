from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from games.models import Game

# Create your views here.

def home_view(request:HttpRequest):

    #get all games
    games = Game.objects.all().order_by("-release_date")[0:3]

    return render(request, 'main/index.html', {"games" : games} )


def contact_view(request:HttpRequest):

    return render(request, 'main/contact.html' )



def mode_view(request:HttpRequest, mode):

    response = redirect(request.GET.get("next", "/"))

    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")


    return response



def test_params_view(request:HttpRequest, param1, param2):

    print(param1, param2)

    if "query_param1" in request.GET:
        query_param1 = request.GET["query_param1"]
        print("Query Parameter 1", query_param1)

    return render(request, "main/test_params.html", {"param1" : param1})