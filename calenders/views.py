from django.shortcuts import render

# Create your views here.

def general(request):
    client = request.user.client
    posts = client.client_posts.all()
    context = {'posts': posts}
    return render(request,"calenders/calenderListing.html",context)