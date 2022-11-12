from django.shortcuts import render, get_object_or_404, redirect

from .models import Note
from .forms import NoteModelForm

def note_list_view(request):
    form = NoteModelForm()
    if request.method == 'POST':
        form = NoteModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note-list')
    active_notes = Note.objects.filter(finished=False)
    finished_notes = Note.objects.filter(finished=True)
    context_page = {
        'notes': active_notes,
        'finished_list': finished_notes,
        'form': form
    }
    return render(request, 'note_list.html', context_page)

def finish_item(request, id):
    note = get_object_or_404(Note, id=id)
    note.finished = True
    note.save()
    return redirect('note-list')

def recover_item(request, id):
    note = get_object_or_404(Note, id=id)
    note.finished = False
    note.save()
    return redirect('note-list')

def delete_item(request, id):
    note = get_object_or_404(Note, id=id)
    note.delete()
    return redirect('note-list')

