from django.shortcuts import render

# Create your views here.
def postt(request):
          context = { 'title' : 'post' }
          return  render(request,'sample_post/post.html',context)
