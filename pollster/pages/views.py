from django.shortcuts import render

# Create your views here.

# Render a landing page
def index(request):
    return render(request, 'pages/index.html')