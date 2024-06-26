from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing


def index(request):

    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def view_listing(request, listing_id):
    listing = Listing.objects.get(name=listing_id)
    return render(request, "auctions/listing.html", {
        "listing": listing
    })

def add_listing(request):
    if request.method == "POST":
        #On recepu les enregistrements
        name = request.POST.get('name')
        comment = request.POST.get('comment')
        price = request.POST.get('price')
        category = request.POST.get('category')

        # Créer un nouveau listing dans la base de donnée en utilisant la Model Listing
        listing = Listing(name=name, comment=comment, price=price, category=category)
        listing.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/add_listing.html")
 #       return render(request, "auctions/listing.html", {
 #           "listing": listing
 #       })
#    else:
 #       return render(request, "auctions/add_listing.html", {"listing": listing
 #       })
