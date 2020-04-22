from django.shortcuts import render
from .models import GmatModel
from django.utils import timezone

def gmat_list(request):
    posts = GmatModel.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'gmat/gmat_list.html', {'posts': posts})
