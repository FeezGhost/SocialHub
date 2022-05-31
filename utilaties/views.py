import datetime
from django.shortcuts import render

# Create your views here.


def getMonths(date):
    currentMonth = int(date.strftime("%m"))
    currentYear = int(date.strftime("%Y"))
    thisMonthDate = datetime.date(year=currentYear,month=currentMonth,day=1)
    nextMonthDate = datetime.date(year=currentYear,month=(currentMonth+1),day=1)
    return thisMonthDate, nextMonthDate
    
def getUserMonthPosts(request, date):
    user = request.user.client
    thisMonthDate, nextMonthDate = getMonths(date)
    products = user.client_posts.all().filter(dateToBuy__gte=thisMonthDate,dateToBuy__lt=nextMonthDate)
    return products