from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def singup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # Gets the POST from from the request and parses it as a UserCreationForm
        if form.is_valid():
            user = form.save()
            #log the user in
            login(request,user)
            return redirect('games:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/singup.html', {"form": form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user= form.get_user()
            login(request, user)
            # Conditional redirect if there is a next property on the request
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('games:list')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('games:list')
