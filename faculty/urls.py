from django.urls import path
from . import views

app_name = "faculty"

urlpatterns = [
    path("", views.home, name="home"),
    path("departments/", views.departments, name="departments"),
    path("departments/<int:id>/", views.department_id, name="department_id"),
    path("programs/", views.programs, name="programs"),
    path("programs/<int:id>/", views.prog_id, name="program_id")
]
