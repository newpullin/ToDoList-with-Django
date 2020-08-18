from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
# Create your views here.

def index(request):
    todos = Todo.objects.all()
    content = {'todos': todos}
    return render(request, 'my_to_do_app/index.html', content)


def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))
    #return HttpResponse(user_input_str)

def doneTodo(request):

    if '완료' == request.GET['btn_type']:
        done_todo_id = request.GET['todoNum']
        print("완료한 todo의 id: ", done_todo_id)
        todo = Todo.objects.get(id = done_todo_id)
        todo.isDone = not todo.isDone
        todo.save()
    elif '수정' == request.GET['btn_type']:
        update_todo_id = request.GET['todoNum']
        todo = Todo.objects.get(id=update_todo_id)
        if todo.isUpdate :
            todo.content = request.GET['editContent']
            todo.isUpdate = False
            todo.save()
        else:
            for obj in Todo.objects.all():
                obj.isUpdate = False
                obj.save()
            todo.isUpdate = True
            todo.save()



    return HttpResponseRedirect(reverse('index'))