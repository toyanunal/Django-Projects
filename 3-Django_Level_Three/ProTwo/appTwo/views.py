from django.shortcuts import render
from appTwo.forms import NewUserForm

# Create your views here.

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request, 'appTwo/help.html', context=helpdict)

def index(request):
    return render(request, 'appTwo/index.html')

def users(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR, FORM INVALID')
    return render(request, 'appTwo/users.html', {'form':form})
