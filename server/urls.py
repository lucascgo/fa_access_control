from django.urls import path

from . import views

urlpatterns = [
    path("api/AcsDataApi/RequestCardEvent", views.qrcode, name="qrcode"),
    path("api/AcsDataApi/RequestStatus", views.heartbeat, name="heartbeat"),
]