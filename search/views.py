from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .filters import LogFilter
from .models import Log
# Create your views here.

@login_required
def index(request):
    Logs = Log.objects.all().order_by('-id')
    logFilter = LogFilter(queryset=Logs)

    if request.method == 'POST':
        logFilter = LogFilter(request.POST, queryset=Logs)

    context = {
        'LogFilter':logFilter
    }
    return render(request, 'search/homepage.html', context)