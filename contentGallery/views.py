from unicodedata import name
from django.shortcuts import render
from contentGallery.dtos import UserPostListResponseDto
from contentGallery.models import PostAlbum
from .forms import PostAlbumForm
from content_libraries.forms import UserPostForm

from content_libraries.models import UserPost

from django.core.paginator import Paginator, EmptyPage
# for multiple clients use 
#     posts = clients.prefetch_related('client_posts')

def gallery(request):
    albumForm = UserPostForm()
    client = request.user.client
    userPosts = client.client_posts.all()
    userpostResponseDto = []

    for userp in userPosts:
        userpostResponse =  UserPostListResponseDto(
            title = userp.title,
            picture = userp.picture,
            smHeight = 300 if userp.picture.height > 300 else userp.picture.height,
            smWidth = 450 if userp.picture.width > 550 else userp.picture.width,
            dateToBuy = userp.dateToBuy
        )
        print("post id", userp.id)
        userpostResponseDto.append(userpostResponse)
    p  = Paginator(userpostResponseDto, 11)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    context = {'userPosts': page}
    return render(request, "contentGallery/default-gallery.html", context=context)


def contentDetails(request, pk_id):
    albumForm = UserPostForm()
    client = request.user.client
    uPost = UserPost.objects.get(id=pk_id)
    context = {'userPost': uPost}
    return render(request, "contentGallery/contentDetails.html", context=context)


def createAlbum(request):
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
    context = {'albumForm': albumForm}
    return render(request, "contentGallery/newalbum.html", context=context)


def albumList(request):
    client = request.user.client
    clientAlbums = client.client_albums.all()
    albums = PostAlbum.objects.all()
    context = {'albums': clientAlbums}
    return render(request, "contentGallery/albums.html", context=context)