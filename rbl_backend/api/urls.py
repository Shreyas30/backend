from django.urls import path
from api import views

urlpatterns = [
    path("insert_dataset", views.insert_dataset, name="InsertDataset"),
    path("fetch_dataset", views.get_all_dataset, name="FetchDataset")
]