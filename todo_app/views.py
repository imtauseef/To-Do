from django.shortcuts import render
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    data = Todo.objects.all().order_by('-date_published')
    content = {
        'data': data,
    }
    return render(request, 'todo_app/home_page.html', content)


def create_item(request):
    user_text = request.POST['text-item']
    entry_date = timezone.now()
    Todo.objects.create(text=user_text, date_published=entry_date)
    return HttpResponseRedirect('/')


def delete_item(request, pk):
    item = Todo.objects.get(id=pk)
    item.delete()
    return HttpResponseRedirect('/')