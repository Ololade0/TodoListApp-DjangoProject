from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import *
from .forms import todo_task
from django.utils import timezone
from builtins import ValueError
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'signupuser.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'signupuser.html', {'form': UserCreationForm, 'error': 'username not found'})
        else:
            return render(request, 'signupuser.html', {'form': UserCreationForm, 'error': 'password not same'})


def loginuser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")

        return render(request, 'currenttodos')
    return render(request, "loginuser.html")


def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect(home)


def currenttodos(request):
    todos = tasklist.objects.filter(user=request.user, dateCompleted__isnull=True)
    return render(request, 'currenttodos.html', {'todos': todos})


def completedtodo(request):
    todo = tasklist.objects.filter(user=request.user, dateCompleted__isnull=False).order_by('-dateCompleted')
    return render(request, 'completedtodos.html', {'todos': todo})


@login_required
def createtodo(request):
    if request.method == 'GET':
        return render(request, 'createtodo.html', {'form': todo_task})
    else:
        try:
            form = todo_task(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'createtodo.html', {'form': todo_task, 'error': 'value exceed'})


def viewtodo(request, todo_pk):
    todos = get_object_or_404(tasklist, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        todoform = todo_task(instance=todos)
        return render(request, 'viewtodo.html', {'todo': todos, 'form': todoform})
    else:
        try:
            form = todo_task(request.POST, instance=todos)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'viewtodo.html', {'todos': todos, 'form': todoform, 'error': 'value error'})


def completetodo(request, todo_pk):
    todos = get_object_or_404(tasklist, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todos.datecompleted = timezone.now()
        todos.save()
        return redirect('currenttodos')


@login_required
def deletetodo(request, todo_pk):
    todos = get_object_or_404(tasklist, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todos.delete()
        return redirect('currenttodos')
