from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def system_settings(request):
    return render(request, "settings_app/system_settings.html")
