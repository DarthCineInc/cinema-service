from django.urls import path
import cinemas.views as views

urlpatterns = [
    path('cinemas', views.cinema_index, name="cinemas_index"),
    path('cinemas/<int:id>', views.cinema_by_id, name="cinemas_by_id"),
]