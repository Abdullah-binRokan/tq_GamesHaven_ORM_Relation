from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Publisher
from .forms import PublisherForm
from games.models import Game

# Create your views here.
def add_publisher_view(request: HttpRequest):
    if request.method == "POST":
        publisher_form = PublisherForm(request.POST, request.FILES)
        if publisher_form.is_valid():
            publisher_form.save()
            return redirect("publishers:all_publishers_view")
        else:
            print("form error: ", PublisherForm.errors)

    return render(request, "publishers/add.html")


def all_publishers_view(request: HttpRequest):
    publishers = Publisher.objects.all()

    return render(request, "publishers/all.html", {"publishers": publishers})

def detail_publisher_view(request: HttpRequest, publisher_id: int):
    publisher = Publisher.objects.get(pk=publisher_id)

    return render(request, "publishers/detail.html", {"publisher": publisher})