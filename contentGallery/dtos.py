
import numbers
from contentGallery.models import PostAlbum


class UserPostListResponseDto:
    def __init__(self, title, pk_id, picture, smHeight, smWidth, dateToBuy):
        self.title = title
        self.pk_id = pk_id
        self.picture = picture
        self.dateToBuy = dateToBuy
        self.smHeight = smHeight
        self.smWidth  = smWidth

        
class AlbumsListResponseDto:
    def __init__(self, album: PostAlbum, posts_count:numbers):
        self.album = album
        self.posts_count = posts_count