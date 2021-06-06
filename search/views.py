from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .filters import LogFilter
from .models import Log
# Create your views here.

@login_required
def index(request):
    Logs = Log.objects.all().order_by('datetime')
    logFilter = LogFilter(
                      request.POST,
                      queryset=Logs
                  )
    paginator = Paginator(logFilter.qs, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # if request.method == 'POST':
    #     logFilter = LogFilter(request.POST, queryset=Logs)

    context = {
        'LogFilter':logFilter,
        'page_obj': page_obj
    }
    return render(request, 'search/homepage.html', context)