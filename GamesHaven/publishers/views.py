from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def add_publisher_view(request: HttpRequest):

    return render(request, "publishers/add.html")