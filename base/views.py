from django.shortcuts import render, redirect
from .models import Note, NoteType
from .forms import NoteForm, NoteFormType, UserForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

@login_required
def home(request):
    note_objs = Note.objects.filter(user=request.user.id).order_by("id")
    note_type_objs = NoteType.objects.all().order_by("id")
    data = {"notes":note_objs, "note_types":note_type_objs}
    
    # print(request)
    # print()
    # print(data["notes"][0].type.name)
    # print()
    return render(request, "index.html", context=data)

@login_required
def note_type(request):
    note_objs = Note.objects.all()
    data = {"notes":note_objs}
    return render(request, "type.html", context=data)

# def create_note(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         description = request.POST.get("description")
#         type_id = request.POST.get("type")

#         n_t_obj = NoteType.objects.get(id=type_id)
#         # print(request)

#         Note.objects.create(name=name, description=description, type=n_t_obj)

#     note_type_objs = NoteType.objects.all()
#     data = {"note_types": note_type_objs}
#     return render(request, "create_note.html", context=data)

@login_required
def create_note(request):
    note_form_obj = NoteForm()
    if request.method == "POST":
        note_form_obj = NoteForm(data=request.POST)
        if note_form_obj.is_valid():
            note_obj = note_form_obj.save()
            note_obj.user = request.user
            note_obj.save()
            messages.success(request, "Note Created Successfully")
            return redirect("home")
        else:
            messages.error(request, note_form_obj.errors)
    data = {"form": note_form_obj}
    return render(request, "create_note.html", context=data)

@login_required
def create_notetype(request):
    notetype_form_obj = NoteFormType()
    if request.method == "POST":
        notetype_form_obj = NoteFormType(data=request.POST)
        if notetype_form_obj.is_valid():
            notetype_form_obj.save()
    data = {"form_type": notetype_form_obj}
    return render(request, "create_notetype.html", context=data) 

@login_required
def edit_note(request, pk):
    note_obj = Note.objects.get(id=pk)
    if request.method == "POST":
        form_obj = NoteForm(instance=note_obj, data=request.POST) # old data is instance and new updating data is data
        if form_obj.is_valid():
            form_obj.save()
    form_obj = NoteForm(instance=note_obj) #instance here is used to display old data in fields when we click the edit button
    data = {"form": form_obj}
    return render(request, "edit_note.html", context=data)

@login_required
def delete_note(request, pk):
    note_obj = Note.objects.get(id=pk)
    note_obj.delete()
    return redirect("home")

@login_required
def delete_all_note(request):
    note_obj = Note.objects.all()
    note_obj.delete()
    return redirect("home")

def register(request):
    if request.method == "POST":
        password = request.POST.get("password")
        hash_password = make_password(password)
        data = request.POST.copy()
        data["password"] = hash_password
        user_form_obj = UserForm(data=data)
        if user_form_obj.is_valid():
            user_form_obj.save()
            return redirect("login")
    user_form_obj = UserForm()
    data = {"form": user_form_obj}
    return render(request, "register.html", context=data)

def user_login(request):
    if request.method == "POST":
        user_username =request.POST.get("username")
        user_password = request.POST.get("password")
        user = authenticate(username=user_username, password=user_password)

        if user != None:
            login(request, user)
            return redirect("home")

    user_form_obj = UserForm()
    data = {"form": user_form_obj}
    return render(request, "login.html", context=data)