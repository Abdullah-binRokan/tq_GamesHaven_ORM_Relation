from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Publisher
from .forms import PublisherForm

# Create your views here.
def add_publisher_view(request: HttpRequest):
    if request.method == "POST":
        publisher_form = PublisherForm(request.POST, request.FILES)
        if publisher_form.is_valid():
            publisher_form.save()
            # return redirect("")
        else:
            print("form error: ", PublisherForm.errors)

    return render(request, "publishers/add.html")