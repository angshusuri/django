from django.shortcuts import render
from . models import Dgotest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def home(request):
          posts = Dgotest.objects.all()
          page = request.GET.get('page', 1)


          paginator = Paginator(posts, 3)
          try:
               posts = paginator.page(page)
          except PageNotAnInteger:
               posts = paginator.page(1)
          except EmptyPage:
               posts = paginator.page(paginator.num_pages)

          context = { 'title' : 'home',
                       'posts': posts }


          return  render(request,'dgotest/index.html', context)
