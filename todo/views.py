from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Todo

# Create your views here.

def home_page(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    context = {
        "todo_items": todo_items
    }
    return render(request, 'todo/index.html', context=context)


def add_todo(request):
    content = request.POST["content"]
    Todo.create(content).save()
    return HttpResponseRedirect("/")

def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
