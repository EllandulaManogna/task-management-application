from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task


@login_required
def dashboard(request):

    if request.method == 'POST':

        title = request.POST['title']
        description = request.POST['description']
        status = request.POST['status']

        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            status=status
        )

        return redirect('dashboard')

    tasks = Task.objects.filter(user=request.user)

    return render(
        request,
        'dashboard.html',
        {'tasks': tasks}
    )


@login_required
def complete_task(request, id):

    task = get_object_or_404(
        Task,
        id=id,
        user=request.user
    )

    task.status = 'Completed'
    task.save()

    return redirect('dashboard')


@login_required
def delete_task(request, id):

    task = get_object_or_404(
        Task,
        id=id,
        user=request.user
    )

    task.delete()

    return redirect('dashboard')


@login_required
def edit_task(request, id):

    task = get_object_or_404(
        Task,
        id=id,
        user=request.user
    )

    if request.method == 'POST':

        task.title = request.POST['title']
        task.description = request.POST['description']
        task.status = request.POST['status']

        task.save()

        return redirect('dashboard')

    return render(
        request,
        'edit_task.html',
        {'task': task}
    )