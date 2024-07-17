from django.shortcuts import render ,HttpResponse

def index(request):
    
    context={
        "variable":"Hello dost!!"

    }
    return render(request,'main.html',context)

def empty(request):
    return HttpResponse("Empty page")

def services(request):
    return render(request,'services.html')