from django.urls import path

from .views import MenuListView, MenuCreateView, MenuDetailView

urlpatterns = [
    path("list/", MenuListView.as_view()),
    path("create/", MenuCreateView.as_view()),
    path("detail/<int:pk>/", MenuDetailView.as_view()),
]
