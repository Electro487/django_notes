from django.shortcuts import render, redirect
from .models import Note, NoteType
from .forms import NoteForm, NoteFormType


# Create your views here.

def home(request):
    note_objs = Note.objects.all()
    data = {"notes":note_objs}
    # print(request)
    # print()
    # print(data["notes"][0].type.name)
    # print()
    return render(request, "index.html", context=data)

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

def create_note(request):
    note_form_obj = NoteForm()
    if request.method == "POST":
        note_form_obj = NoteForm(data=request.POST)
        # print(note_form_obj)
        if note_form_obj.is_valid():
            note_form_obj.save()
    data = {"form": note_form_obj}
    return render(request, "create_note.html", context=data)

def create_notetype(request):
    notetype_form_obj = NoteFormType()
    if request.method == "POST":
        notetype_form_obj = NoteFormType(data=request.POST)
        # print(notetype_form_obj)
        if notetype_form_obj.is_valid():
            notetype_form_obj.save()
    data = {"form_type": notetype_form_obj}
    return render(request, "create_notetype.html", context=data) 

def edit_note(request, pk):
    note_obj = Note.objects.get(id=pk)
    if request.method == "POST":
        form_obj = NoteForm(instance=note_obj, data=request.POST)
        if form_obj.is_valid():
            form_obj.save()
    form_obj = NoteForm(instance=note_obj)
    data = {"form": form_obj}
    return render(request, "edit_note.html", context=data)

def delete_note(request, pk):
    note_obj = Note.objects.get(id=pk)
    note_obj.delete()
    return redirect("home")

def delete_all_note(request):
    note_obj = Note.objects.all()
    note_obj.delete()
    return redirect("home")