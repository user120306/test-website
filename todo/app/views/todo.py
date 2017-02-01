from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from .forms import *
from django.template import RequestContext
from django.shortcuts import render_to_response

def add_todo(request):
    if request.method=='POST':
        todo_obj=Todo(todo_job=request.POST.get('job'),user_id=request.session['user_id'])
        todo_obj.save()
        return HttpResponseRedirect('/')
    else:
        data=RequestContext(request,{'fname':request.session['fname']})
        return render_to_response('add_todo.html',data)

def edit_todo(request,todo_id):
    if request.method=='POST':
        todo_obj=Todo.objects.filter(id=request.POST.get('id')).update(todo_job=request.POST.get('job'))
        return HttpResponseRedirect('/')
    else:
        todo_obj=Todo.objects.filter(id=todo_id)
        data=RequestContext(request,{'fname':request.session['fname'],'todo':todo_obj[0]})
        return render_to_response('edit_todo.html',data)

def delete_todo(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')