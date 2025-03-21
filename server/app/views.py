from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.


def hello(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        return request.POST.get("name", "No name provided")

    elif request.method == "GET":
        return render(request, "Index.html", {"name": "Django"})
