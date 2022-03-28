from django.urls import path
from . import views

app_name = "notes"
urlpatterns = [
    path('', views.index, name="index"),
    path('notes/', views.notes, name="notes"),
    path('<int:note_id>/', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('create/<int:note_id>', views.createContent, name="create_content"),
    path('<int:note_id>/<int:content_id>/delete', views.delete, name="delete"),
    path('<int:note_id>/delete', views.delete_note, name="delete_note"),
    path('<int:note_id>/<int:content_id>/', views.content, name="content"),
    path('login/', views.login, name="login"),
    path('register/', views.registrate, name="registrate"),
    path('edit/<int:note_id>', views.edit_note, name="edit_note"),
]
