from django.shortcuts import render

# Create your views here.
def Index_view(request):
      return render(request,"index.html")   