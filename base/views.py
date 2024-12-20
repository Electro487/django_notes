from django.shortcuts import render
from .models import Note, NoteType


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

def create_note(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        type_id = request.POST.get("type")

        n_t_obj = NoteType.objects.get(id=type_id)
        # print(request)

        Note.objects.create(name=name, description=description, type=n_t_obj)

    note_type_objs = NoteType.objects.all()
    data = {"note_types": note_type_objs}
    return render(request, "create_note.html", context=data)
