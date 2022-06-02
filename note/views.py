from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Category, Note
from .forms import NoteForm, CreteCategory
# Create your views here.


@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
    categories = Category.objects.filter(host=request.user)
    if len(categories) == 0:
        return redirect('noteapp:category-page')
    notes = Note.objects.filter(author=request.user)
    context = {'notes': notes, 'categories': categories}
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
        else:
            print('something is error')
    categories = Category.objects.filter(host=request.user)
    return render(request, 'note/create_note.html', {'categories': categories})


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
    categories = Category.objects.filter(host=request.user)
    context = {'title': note.title,
               'desc': note.desc, 'categories': categories}
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form = form.save()
            return redirect('noteapp:home')

    return render(request, 'note/update_note.html', context)


def create_category(request):
    if request.method == 'POST':
        form = CreteCategory(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.host = request.user
            form.save()
            return redirect('noteapp:home')

    return render(request, 'note/create_category.html')


def category_page(request):
    categoery = Category.objects.filter(host=request.user)
    if request.method == 'POST':
        form = CreteCategory(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.host = request.user
            form.save()
        return redirect('noteapp:category-page')
    return render(request, 'note/category_page.html', context={'categoery': categoery})


def delete_category(request, pk):
    # get categoey
    categoery = Category.objects.get(id=pk)
    categoery.delete()
    return redirect('noteapp:category-page')


def template(request):
    return render(request, 'note/note_component.html')
