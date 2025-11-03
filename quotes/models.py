from django.db import models

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    genre = models.CharField(
        max_length=100,
        choices=[
            ('inspiration', 'Inspiration'),
            ('love', 'Love'),
            ('humor', 'Humor'),
            ('life', 'Life'),
            ('friendship', 'Friendship'),
        ],
        default='inspiration'
    )
    like = models.IntegerField(default=0)
    liked_by = models.ManyToManyField('auth.User', related_name='liked_quotes', blank=True)

    def __str__(self):
        return f"{self.text} - {self.author}"
