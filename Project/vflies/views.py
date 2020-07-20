from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("Fly, Virtual Flies, Fly!")
    return render(request, 'vflies/page.html')

