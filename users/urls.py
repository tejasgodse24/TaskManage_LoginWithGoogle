from django.urls import path
from users.views import *

urlpatterns = [
    path("", index, name="home_view"),
    path("adminpanel/", admin_view, name="admin_view"),
    path("adminpanel/add", addedit_credential, name="add_credential"),
    path("adminpanel/edit/<int:id>", addedit_credential, name="edit_credential"),
    path("adminpanel/delete/<int:id>", delete_credential, name="delete_credential"),
    path("adminpanel/change/<int:id>", change_credential, name="change_credential"),
    path("logout/", logout_view, name="logout"),

    path("inviteusers/", invite_users, name="invite_user"),


]
