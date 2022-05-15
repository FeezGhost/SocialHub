from django.shortcuts import render
from contentGallery.dtos import UserPostListResponseDto

from content_libraries.models import UserPost

# for multiple clients use 
#     posts = clients.prefetch_related('client_posts')
def gallery(request):
    client = request.user.client
    userPosts = client.client_posts.all()
    userpostResponseDto = []
    for userp in userPosts:
        userpostResponse =  UserPostListResponseDto(
            title = userp.title,
            picture = userp.picture,
            smHeight = 300 if userp.picture.height > 300 else userp.picture.height,
            smWidth = 550 if userp.picture.width > 550 else userp.picture.width,
            dateToBuy = userp.dateToBuy
        )
        userpostResponseDto.append(userpostResponse)

    context = {'userPosts': userpostResponseDto}
    print(context)
    return render(request, "contentGallery/default-gallery.html", context=context)