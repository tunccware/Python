from django.urls import path
from . import views
app_name = "menu"
urlpatterns=[
    path('', views.food_list ,name = "food_list"),
    path('<int:id>/', views.food_detail, name="food_detail"),
    path("reservation/", views.reservation, name="reservation"),
    path("contact/", views.contact, name="contact"),
    path(
    "reservation/success/<int:reservation_id>/",
    views.reservation_success,
    name="reservation_success"
),
]
