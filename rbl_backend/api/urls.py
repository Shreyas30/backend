from django.urls import path
from api import views

urlpatterns = [
    path("insert_dataset", views.insert_dataset, name="InsertDataset"),
    path("describe_dataset", views.describe_dataset, name="DescribeDataset")
]