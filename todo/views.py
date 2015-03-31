from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from forms import *
from models import *

# Create your views here.
def list(request):
    todo = Todo.objects.all()
    return render(request, 'index.html', {'list': todo})

def add(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('list'))
    else:
        form = TodoForm()
    return render(request, 'add.html', {'form': form})

def edit(request, **kwargs):
    pk = kwargs.get('pk')
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            form = TodoForm()
            return redirect(reverse('list'))
    else:
        form = TodoForm(instance=todo)
    return render(request, 'add.html', {'form': form})

def delete(request, **kwargs):
    pk = kwargs.get('pk')
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        todo.delete()
        return redirect(reverse('list'))
    return render(request, 'delete.html', {'todo': todo})