from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError

from lists.models import Item, List
from lists.forms import ExistingListItemForm, ItemForm

def home_page(request):
	return render(request, 'home.html', {'form': ItemForm()})

def view_list(request, list_id):
	list = List.objects.get(id=list_id)
	if request.method == 'POST':
		form = ExistingListItemForm(data={
			'text': request.POST['text'],
			'list': list.id
		})
		if form.is_valid():
			form.save()
			return redirect('/lists/%d/' % (list.id,))
	else:
		form = ExistingListItemForm()
	return render(request, 'list.html', {'list': list, "form": form})

def new_list(request):
	form = ItemForm(data=request.POST)
	if form.is_valid():
		list = List.objects.create()
		Item.objects.create(text=request.POST['text'], list=list)
		return redirect('/lists/%d/' % (list.id,))
	else:
		return render(request, 'home.html', {"form": form})


def add_item(request, list_id):
	list = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['text'], list=list)
	return redirect('/lists/%d/' % (list.id,))
