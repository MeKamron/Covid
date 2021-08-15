from django.shortcuts import render

from .models import Client


def client_list(request):
    clients = Client.objects.all()
    return render(request, "list.html", {"clients": clients})

def detail(request, id):
    client = Client.objects.get(id=id)
    return render(request, f"{client.qayerga.lower()}.html", {"client": client})

def new_client(request):
    if request.method == "POST":
        pass
