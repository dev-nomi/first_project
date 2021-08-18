from django.shortcuts import render,redirect
#later on we get tasks from db
tasks = ['New Ruby task' , 'New Python task' , 'New Java task']

# Create your views here.
def index(request):
  return render(request,'tasks/index.html',{
    "tasks" : tasks
  })

def new(request):
  if request.method == "POST":
    tasks.append(request.POST.get("task"))
    return redirect('tasks:index')
  return render(request,'tasks/new.html')

  

