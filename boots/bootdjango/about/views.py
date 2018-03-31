from django.shortcuts import render

# Create your views here.
def about(response):
          context = { 'title' : 'about' }
          return render(response,'about/about.html', context)
