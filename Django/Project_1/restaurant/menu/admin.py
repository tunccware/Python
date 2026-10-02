from django.contrib import admin
from .models import Food, Category, Reservation


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    fields = ("name", "price", "description", "image", "category")

admin.site.register(Reservation)