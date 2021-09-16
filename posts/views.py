from django.shortcuts import render

# Create your views here.
#Home
def Home(request):
    return render(request, 'base.html')