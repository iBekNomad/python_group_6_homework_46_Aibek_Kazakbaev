from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Article, STATUS_CHOICES
from django.http import HttpResponseNotAllowed


def index_view(request):
    data = Article.objects.all()
    return render(request, 'index.html', context={
        'articles': data
    })


def task_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {'article': article}
    return render(request, 'task_view.html', context)


def task_create_view(request):
    if request.method == 'GET':
        return render(request, 'task_create.html', context={
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        description = request.POST.get('description')
        text = request.POST.get('text')
        status = request.POST.get('status')
        date = request.POST.get('created_at')
        article = Article.objects.create(description=description, text=text, status=status, created_at=date)
        return redirect('task_view', pk=article.pk)
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
