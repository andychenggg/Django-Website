from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import ToDoList
from .forms import CreateListForm
# Create your views here.

def index(request, id):
	ls = ToDoList.objects.get(id=id)

	if request.method == "POST":
		if request.POST.get("save"):
			for item in ls.item_set.all():
				p = request.POST
				
				if "clicked" == p.get("c"+str(item.id)):
					item.complete = True
				else:
					item.complete = False

				if "text" + str(item.id) in p:
					item.text = p.get("text" + str(item.id))


				item.save()

		elif request.POST.get("add"):
			newItem = request.POST.get("new")
			if newItem != "":
				ls.item_set.create(text=newItem, complete=False)
			else:
				print("invalid")

		elif "delete" in request.POST:
			item_id = int(request.POST["delete"])
			item = ls.item_set.get(id=item_id)
			item.delete()

	return render(request, "main/index.html", {"ls": ls})


def get_name(request):
	if request.method == "POST":
		form = CreateListForm(request.POST)

		if form.is_valid():
			n = form.cleaned_data["name"]
			t = ToDoList(name=n, date=timezone.now())
			t.save()
			
			return HttpResponseRedirect("/%i" %t.id)

	else:
		form = CreateListForm()

	return render(request, "main/create.html", {"form": form})


def home(request):
	return render(request, "main/home.html", {})


def view(request):
	l = ToDoList.objects.all()
	return render(request, "main/view.html", {"lists":l})

def delete_list(request, id):
    if request.method == "POST":
        ls = get_object_or_404(ToDoList, id=id)
        ls.delete()
        return HttpResponseRedirect("/view")  # 重定向到清单列表页面
    return HttpResponseRedirect("/view")  # 如果不是POST请求，也重定向到列表页面

