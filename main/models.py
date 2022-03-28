from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateTimeField, EmailField, TextField
from django.db.models.fields.related import ForeignKey


class Note(models.Model):
    note_title = CharField(max_length=200)

    def __str__(self):
        return self.note_title


class Content(models.Model):
    Note = ForeignKey(Note, on_delete=models.CASCADE)
    note_text = TextField(max_length=10000)
    date_pub = DateTimeField()
    tags = CharField(max_length=200)

    def __str__(self):
        return self.note_text


class User(models.Model):
    username = CharField(max_length=200)
    password = CharField(max_length=200)
    email = EmailField(max_length=200)

    def __str__(self):
        return self.username
