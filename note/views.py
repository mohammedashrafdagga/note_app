from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm
# Create your views here.


@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()

    notes = Note.objects.filter(author=request.user)
    context = {'notes': notes}
    return render(request, 'note/home.html', context=context)


@login_required(login_url='login')
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('noteapp:home')
    return render(request, 'note/create_note.html')


@login_required(login_url='login')
def delete_note(request):
    if request.method == 'POST':
        note_id = request.POST.get('delete_id')
        note = Note.objects.filter(id=note_id).first()
        if note and request.user == note.author:
            note.delete()
            return redirect('noteapp:home')


@login_required(login_url='login')
def update_note(request, pk):
    note = Note.objects.get(id=pk)
    form = NoteForm(request.POST, instance=note)
    context = {'title': note.title, 'desc': note.desc}
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form = form.save()
            return redirect('noteapp:home')
    return render(request, 'note/update_note.html', context)
