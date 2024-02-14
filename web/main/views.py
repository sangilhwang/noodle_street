from django.shortcuts import render

# Create your views here

def main(request):
    return render(request, 'main/main.html')

def test(request):
    return render(request, 'main/test5.html')