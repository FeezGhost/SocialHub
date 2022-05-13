import datetime
from django.shortcuts import redirect, render
from .forms import UserPostForm

from .models import Tag, UserPost
from geopy.geocoders import Nominatim
from dateutil import parser
from django.utils.timezone import make_aware

# Create your views here.

def addPostTags(tags: str, Id):
    tagsList = tags.split(",")
    uPost = UserPost.objects.get(id=Id)
    PostTags = Tag.objects.only('name').filter(user_post_id=Id)
    if len(tagsList) > 0:
        if tagsList[len(tagsList)-1] == " ":
            tagsList = tagsList.remove('')
        tagsList = list(dict.fromkeys(tagsList))
        for tag in tagsList:
            if tag not in PostTags and tag != '':
                tagObj = Tag.objects.create(
                    user_post = uPost,
                    name = tag
                )

def createPost(request):
    form = UserPostForm()
    if request.method == 'POST':
        locator = Nominatim(user_agent="myGeocoder")
        form = UserPostForm(request.POST)
        if form.is_valid():
            f_title = form.cleaned_data.get('title')
            f_description = form.cleaned_data.get('description')
            f_location = form.cleaned_data.get('location')
            latitude = request.POST.get('lat')
            latitude = 0 if latitude == '' else float(latitude)
            longitude = request.POST.get('lng')
            longitude = 0 if longitude =='' else float(longitude)
            coordinates = str(latitude) + ", " + str(longitude)
            if(f_location == '' or f_location == None): 
                geo_location = locator.reverse(coordinates)
                f_location = geo_location.address
            else :
                geo_location = locator.geocode(f_location)
                latitude = float(geo_location.latitude)
                longitude = float(geo_location.longitude)
            
            date = request.POST.get('startDate')
            tempDate = datetime.datetime.now()
            if date != '':
                tempDate = parser.parse(date)
                # curr_date = datetime.now()
                # curr_date.
                if tempDate < datetime.datetime.now():
                    tempDate = datetime.datetime.now()
                else: 
                    tempDate = make_aware(tempDate)
            userPostObj = UserPost.objects.create(
                title = f_title,
                description = f_description,
                client = request.user.client,
                lat = latitude,
                lng = longitude,
                location = f_location,
                dateToBuy = tempDate
            )
            addPostTags(request.POST.get('tags'), userPostObj.id)
    context = {'form': form}
    return render(request, "content_libraries/facebook_library.html", context)