from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    price = models.CharField(max_length=30)
    score_choices = (
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    )
    # 앞의 값은 detail에 나오는 값, 뒤의 값은 선택지에 뜨는 값 
    score = models.IntegerField(
        choices = score_choices,
        default = 3,
    )
    created_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.book_title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
    content = models.TextField()