from urllib import request
from django.shortcuts import render
from introduce.models import AccessLog

# Create your views here.
def introduce(request):
    # case 1
    """
    access_log = AccessLog()
    access_log.location = "introduce"
    access_log.save()
    """
    # case 2
    AccessLog.objects.create(
        location="introduce"
    )
    
    return render(request, 'introduce.html')
