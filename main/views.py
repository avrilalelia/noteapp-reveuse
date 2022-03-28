from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Note, Content, User
from .forms import CreateNewList, CreateNewContent, Login, Register
from django import forms
from django.urls import reverse
from django.utils import timezone


def index(response):
    return render(response, "main/index.html", {})


def notes(response):
    n = Note.objects.all()
    return render(response, "main/notes.html", {
        "notes": n,
    })


def detail(response, note_id):
    n = get_object_or_404(Note, pk=note_id)
    return render(response, "main/details.html", {
        "note": n,
    })


def content(response, note_id, content_id):
    n = get_object_or_404(Note, pk=note_id)
    c = n.content_set.get(pk=content_id)
    if response.method == 'POST':
        form = CreateNewContent(response.POST)
        if form.is_valid():
            n = form.cleaned_data["text"]
            t = form.cleaned_data["tag"]
            c.note_text = n
            c.tags = t
            c.save()
            return HttpResponseRedirect(reverse('notes:detail', args=(note_id,)))
    else:
        form = CreateNewContent(initial={'text': c.note_text, 'tag': c.tags})
    return render(response, "main/content.html", {
        "form": form,
        'note': n,
    })


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["title"]
            t = Note(note_title=n)
            t.save()
            return HttpResponseRedirect(reverse('notes:detail', args=(t.id,)))
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})


def delete(response, note_id, content_id):
    n = get_object_or_404(Note, pk=note_id)
    c = n.content_set.get(pk=content_id)
    c.delete()
    return HttpResponseRedirect(reverse('notes:detail', args=(note_id,)))


def delete_note(response, note_id):
    n = get_object_or_404(Note, pk=note_id)
    n.delete()
    return HttpResponseRedirect(reverse('notes:notes', args=()))


def edit_note(response, note_id):
    n = get_object_or_404(Note, pk=note_id)
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            n.note_title = title
            n.save()
            return HttpResponseRedirect(reverse('notes:notes'))
    else:
        form = CreateNewList(initial={'title': n.note_title})
    return render(response, "main/edit_note.html", {"form": form, "note_id": n.id})


def createContent(response, note_id):
    if response.method == "POST":
        form = CreateNewContent(response.POST)
        if form.is_valid():
            n = get_object_or_404(Note, pk=note_id)
            text = form.cleaned_data["text"]
            date = timezone.now()
            tag = form.cleaned_data["tag"]
            t = n.content_set.create(note_text=text, date_pub=date, tags=tag)
            return HttpResponseRedirect(reverse('notes:detail', args=(note_id,)))
    else:
        form = CreateNewContent()
    return render(response, "main/create.html", {"form": form})


def registrate(response):
    if response.method == "POST":
        form = Register(response.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            n = User(username=username, password=password, email=email)
            n.save()
            return HttpResponseRedirect(reverse('notes:login'))
    else:
        form = Register()
    return render(response, "main/register.html", {
        "form": form
    })


def login(response):
    if response.method == "POST":
        form = Login(response.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            if User.objects.filter(username=username, password=password):
                return HttpResponseRedirect(reverse('notes:notes'))
    else:
        form = Login()
    return render(response, "main/login.html", {
        "form": form
    })
