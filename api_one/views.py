from django.shortcuts import render

# Create your views here.
def new_vista(request):
    return render(request,'index.html')