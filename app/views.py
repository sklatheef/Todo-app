from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from .models import Task_Db, History_Db  

def home(request):
    if request.method == "POST":
        task = request.POST.get('task')
        desc = request.POST.get('desc')
        Task_Db.objects.create(task=task, desc=desc)
        return redirect('display')
    return render(request, 'home.html')

def display(request):
    data = Task_Db.objects.all().order_by('-id')
    return render(request, 'display.html', {'data': data})

def single(request, id):
    task = get_object_or_404(Task_Db, id=id)
    return render(request, 'single.html', {'task': task})

def edit_task(request, id):
    task = get_object_or_404(Task_Db, id=id)
    if request.method == "POST":
        task.task = request.POST.get('task')
        task.desc = request.POST.get('desc')
        task.save()
        return redirect('display')
    return render(request, 'edit.html', {'task': task})

def delete_task(request, id):
    task_obj = get_object_or_404(Task_Db, id=id)
    
    if request.method == "POST":
        # The actual logic happens here after the user clicks "Yes"
        with transaction.atomic():
            History_Db.objects.create(
                task=task_obj.task,
                desc=task_obj.desc
            )
            task_obj.delete()
        return redirect('display')
    
    # If they just clicked the link, show them the confirmation page
    return render(request, 'delete.html', {'task': task_obj})

def history(request):
    hist_data = History_Db.objects.all().order_by('-deleted_at')
    return render(request, 'history.html', {'data': hist_data})

def restore_task(request, id):
    hist_obj = get_object_or_404(History_Db, id=id)
    with transaction.atomic():
        Task_Db.objects.create(task=hist_obj.task, desc=hist_obj.desc)
        hist_obj.delete()
    return redirect('display')

def toggle_status(request, id):
    task = get_object_or_404(Task_Db, id=id)
    task.status = not task.status
    task.save()
    return redirect('display')

def about(request):
    return render(request, 'about.html')