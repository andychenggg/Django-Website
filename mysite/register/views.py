from django.shortcuts import render, redirect

from main.models import ToDoList
from .forms import RegisterForm

# Create your views here.
def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			user = form.save(commit=False)
			default_list = ToDoList.objects.create(name="My todo list")
			user.toDoLists = default_list
			user.save()
			return redirect("/home")
	else:
		form = RegisterForm()
		
	return render(response, "register/register.html", {"form":form})