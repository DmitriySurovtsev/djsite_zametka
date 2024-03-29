from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .forms import *
from .models import *
from django.views.generic import ListView
from django.views.generic import DeleteView

# Create your views here.
"""
НЕОБХОДИМО ВЕРНУТЬСЯ НА УРОКИ 3-7, чтобы вспомнить материал
"""

class NoticeHome(ListView): #Отвечает за базовую страницу сайта и основываться на классе ListView
    model = Notice
    template_name = "notice/index.html"
    context_object_name = 'notice_card_information'

# def index(request):
#     notice_card_information = Notice.objects.all()
#     return render(request, 'notice/index.html', {'notice_card_information': notice_card_information})



def add_notice(request):
    if request.method == 'POST':
        form = AddNotice(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = AddNotice()
    return render(request, 'notice/addnotice.html', {'form': form})

def full_notice(request): #по айди отображать карточку в новой странице, где будет возможность edit and delete
    return render(request, 'notice/fullnotice.html')


#exceptions
def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")