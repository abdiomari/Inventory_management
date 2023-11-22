from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "index.html")


def sales(request):
    return render(request, "sales.html")

def purchases(request):
    return render(request, "purchases.html")