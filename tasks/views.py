from django.shortcuts import render

#later on we get tasks from db
tasks = ['New Ruby task' , 'New Python task' , 'New Java task']

# Create your views here.
def index(request):
  return render(request,'tasks/index.html',{
    "tasks" : tasks
  })

def new(request):
  return render(request,'tasks/new.html')
