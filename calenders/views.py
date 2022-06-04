import datetime
from django.shortcuts import render
from django.contrib import messages
from utilaties.views import getUserMonthPosts
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def general(request):
    user = request.user
    client = user.client
    clientAlbums = client.client_albums.all()
    currentDate = datetime.date.today()
    posts = getUserMonthPosts(request, currentDate)
    
    if request.method == "POST":
        date = request.POST.get('monthHiiden')
        if date != None:
            tempDate = datetime.datetime.strptime(date, "%Y-%m-%d")
            newdate = tempDate.strftime("%Y-%m-%d")
            posts = getUserMonthPosts(request, tempDate)
            context = {
                'posts' : posts, 
                "date" : newdate,
                }
            return render(request,"calenders/calenderListing.html",context)
        else:
            messages.error(request, "There was a date issue!")
    context = {
        'posts': posts,  
        "date" : currentDate,
        'user': user, 
        'albums': clientAlbums
        }
    return render(request,"calenders/calenderListing.html",context)