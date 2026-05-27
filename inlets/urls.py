from django.urls import path
from .views import ingest_inlets

urlpatterns = [
    path("inlets/", ingest_inlets),
]