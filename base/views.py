from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("""<h1 style='color:red;'>I am red</h1>\n <h1 style='color:blue;'>I am Best developer</h1> """)
    return render(request, "index.html")

