from unicodedata import name
from django.shortcuts import redirect, render
from contentGallery.dtos import AlbumsListResponseDto, UserPostListResponseDto
from contentGallery.models import PostAlbum
from .forms import PostAlbumForm
from content_libraries.forms import UserPostForm
from django.contrib import messages
from content_libraries.models import UserPost

from django.core.paginator import Paginator, EmptyPage
from dateutil import parser
from django.utils.timezone import make_aware
from django.contrib.auth.decorators import login_required
# for multiple clients use 
#     posts = clients.prefetch_related('client_posts')

@login_required(login_url="login")
def gallery(request):
    user = request.user
    client = user.client
    clientAlbums = client.client_albums.all()
    userPosts = client.client_posts.all()
    userpostResponseDto = []
    albumId = 0
    
    if request.method == 'POST':
        album_id = request.POST.get('album_id')
        print('album_id', album_id)
        if userPosts.exists():
            for clientAlbum in clientAlbums:
                print('clientAlbum',clientAlbum)
                if (clientAlbum.id == int(album_id)):
                    albumId = clientAlbum.id
                    album = PostAlbum.objects.get(id=albumId)
                    print('album', album)
                    userPosts = album.posts.all()
                    
    album_id = request.GET.get('album_id')
    if(album_id is not None):
        album_id = int(album_id)
        if(album_id>0):
            albumId = album_id
            album = PostAlbum.objects.get(id=albumId)
            userPosts = album.posts.all()
    for userp in userPosts:
        userpostResponse =  UserPostListResponseDto(
            title = userp.title,
            pk_id = userp.id,
            picture = userp.picture,
            smHeight = 300 if userp.picture.height > 300 else userp.picture.height,
            smWidth = 450 if userp.picture.width > 550 else userp.picture.width,
            dateToBuy = userp.dateToBuy
        )
        userpostResponseDto.append(userpostResponse)
    p  = Paginator(userpostResponseDto, 11)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    context = {'userPosts': page, 'user': user, 'albums': clientAlbums, 'albumId': albumId}
    return render(request, "contentGallery/default-gallery.html", context=context)


@login_required(login_url="login")
def contentDetails(request, pk_id):
    user = request.user
    client = user.client
    clientAlbums = client.client_albums.all()
    albumForm = UserPostForm()
    uPost = UserPost.objects.get(id=pk_id)
    context = {'userPost': uPost, 'user': user, 'albums': clientAlbums}
    return render(request, "contentGallery/contentDetails.html", context=context)


@login_required(login_url="login")
def postDetailUpdate(request, pk_id):
    userPost = UserPost.objects.get(id = pk_id)
    if request.method == 'POST':
        try:
            date = request.POST.get('productdateTime')
            tempDate = parser.parse(date)
            newdate = make_aware(tempDate)
            userPost.dateToBuy = newdate
            userPost.isSchedule = True
            userPost.save()
            messages.success(request, "Post Has Been Updated!")
        except:
            messages.error(request, "Failed To Update Post!")

    return redirect('contentDetails', pk_id=userPost.id)

@login_required(login_url="login")
def createAlbum(request):
    user = request.user
    client = user.client
    clientAlbums = client.client_albums.all()
    albumForm = PostAlbumForm()
    client = request.user.client
    if request.method == 'POST':
        form = PostAlbumForm(request.POST)
        if form.is_valid():
            f_name = form.cleaned_data.get('name')
            PostAlbum.objects.create(
                client = client,
                name = f_name
            )
            messages.success(request, "Album has been created!")
        else:
            messages.error(request, "Couldn't Create Album!")
    context = {'albumForm': albumForm, 'user': user, 'albums': clientAlbums}
    return render(request, "contentGallery/newalbum.html", context=context)

@login_required(login_url="login")
def albumList(request):
    user = request.user
    client = user.client
    clientAlbums = client.client_albums.all()
    albums = []
    for album in clientAlbums:
        albums.append(AlbumsListResponseDto(
            album = album,
            posts_count = album.posts.all().count()
        ))
    context = {'ualbums': albums,'user': user, 'albums':  clientAlbums}
    return render(request, "contentGallery/albums.html", context=context)