from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView


from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>", views.DetailsView.as_view(), name="details"),
    path("<int:question_id>/vote", views.vote, name="vote"),
    path("login", LoginView.as_view(template_name="admin/login.html"), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
]
