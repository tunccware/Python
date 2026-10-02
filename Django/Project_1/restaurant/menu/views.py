from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Food, Category, Reservation
from .forms import ReservationForm

def home(request):
    return render(request, "home.html")

def food_list(request):
    categories = Category.objects.all()

    return render(
        request,
        "menu/food_list.html",
        {"categories": categories}
    )


def food_detail(request, id):
    food = get_object_or_404(Food, id=id)

    return render(
        request,
        "menu/food_detail.html",
        {"food": food}
    )

def reservation(request):

    if request.method == "POST":
        form = ReservationForm(request.POST)

        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()

        return redirect(
            "menu:reservation_success",
            reservation_id=reservation.id
        )

    else:
        form = ReservationForm()

    return render(
        request,
        "menu/reservation.html",
        {"form": form}
    )

def contact(request):
    return render(request, "menu/contact.html")

def reservation_success(request, reservation_id):
    reservation = get_object_or_404(
    Reservation,
    id=reservation_id
)

    return render(
        request,
        "menu/reservation_success.html",
        {"reservation": reservation}
    )