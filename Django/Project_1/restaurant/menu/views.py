from django.shortcuts import get_object_or_404, render
from .models import Food, Category

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