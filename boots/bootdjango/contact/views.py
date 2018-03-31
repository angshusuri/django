from django.shortcuts import render

# Create your views here.
def contact(response):
          context = { 'title' : 'contact' }
          return render(response,'contact/contact.html', context)
