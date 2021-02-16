from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

# Create your views here.

def home_page(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    context = {
        "todo_items": todo_items
    }
    return render(request, 'todo/index.html', context=context)


def add_todo(request):
    print(request.POST)
    return HttpResponseRedirect("/")
