from django.urls import path
from . import views

urlpatterns = [
   path("", views.index, name="ShopHome"),
   path("about/", views.about, name="about us"),
   path("contact/", views.contact, name="contact us"),
   path("tracker/", views.tracker, name="Traking"),
   path("search/", views.search, name="Search"),
   path("productview/", views.productview, name="Productview"),
   path("checkout/", views.checkout, name="Checkout"),
]