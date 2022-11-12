from django.shortcuts import render, get_object_or_404, redirect

from .models import Note

def note_list_view(request):
    active_notes = Note.objects.filter(finished=False)
    finished_notes = Note.objects.filter(finished=True)
    context_page = {'notes': active_notes, 'finished_list': finished_notes}
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

