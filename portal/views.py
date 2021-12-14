from django.shortcuts import render, get_object_or_404, redirect
from .models import Portal
from .forms import AppForm
from django.utils import timezone


def app_list(request):
    apps = Portal.objects.filter(publish__lte=timezone.now()).order_by('publish')
    return render(request, 'portal/app/list.html', {'apps': apps})


def app_detail(request, pk):
    app = get_object_or_404(Portal, pk=pk)
    return render(request, 'portal/app/detail.html', {'app': app})


def app_new(request):
    form = AppForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            app = form.save(commit=False)
            app.author = request.user
            app.publish = timezone.now()
            app.save()
            return redirect('detail', pk=app.pk)
        else:
            form = AppForm()
    return render(request, 'portal/app/app_edit.html', {'form': form})