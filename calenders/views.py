import datetime
from django.shortcuts import render
from django.contrib import messages
from utilaties.views import getUserMonthPosts

# Create your views here.

def general(request):
    currentDate = datetime.date.today()
    client = request.user.client
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
        }
    return render(request,"calenders/calenderListing.html",context)