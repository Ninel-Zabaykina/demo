from django.shortcuts import render, get_object_or_404
from .models import Portal
from django.utils import timezone


def app_list(request):
    apps = Portal.objects.filter(publish__lte=timezone.now()).order_by('publish')
    return render(request, 'portal/app/list.html', {'apps': apps})


def app_detail(request, year, month, day, app):
    app = get_object_or_404(Portal, title=app,
                            status='publish',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    return render(request, 'portal/app/detail.html', {'app': app})
