import datetime
from io import BytesIO
import sys
from django.shortcuts import render
from .forms import UserPostForm
from .models import Tag, UserPost
from geopy.geocoders import Nominatim
from dateutil import parser
from django.utils.timezone import make_aware
from PIL import Image
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile

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
        form = UserPostForm(request.POST, request.FILES)

        if form.is_valid():
            f_title = form.cleaned_data.get('title')
            f_description = form.cleaned_data.get('description')
            f_location = form.cleaned_data.get('location')
            f_picture = form.cleaned_data.get('picture')
            image = Image.open(f_picture)
            width, height = image.size
            if width > 1500:
                image = image.resize((1500, height))
            
            im_io = BytesIO()
            image.save(im_io, 'JPEG', quality=85)
            im_io.seek(0)
            new_image = InMemoryUploadedFile(im_io,'ImageField', "%s.jpg" %f_picture.name.split('.')[0], 'image/jpeg', sys.getsizeof(im_io), None)
            print(new_image)

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
                dateToBuy = tempDate,
                picture = new_image
            )

            addPostTags(request.POST.get('tags'), userPostObj.id)
            
    context = {'form': form}
    return render(request, "content_libraries/facebook_library.html", context)

