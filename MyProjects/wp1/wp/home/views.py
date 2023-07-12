from django.shortcuts import render , HttpResponse

# Create your views here.
def home(request):
    return render(request,'home/index.html')

def about(request):
    return render(request,'home/index.html') 
# def services(request):
#     return HttpResponse('<h1>Services PAge</h1>')

# def contacts(request):
#     return HttpResponse('<h1>contact PAge</h1>')
