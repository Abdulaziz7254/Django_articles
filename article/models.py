from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Caregory(models.Model):
    title = models.CharField(max_length=50,verbose_name='Category')
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=255 , verbose_name='Article')
    date = models.DateField()
    author = models.CharField(max_length=50, verbose_name='Auther article')
    image = models.ImageField(upload_to='posters', blank=True, null=True, verbose_name='Poster')
    text = models.TextField(verbose_name='Discription: ')
    category = models.ForeignKey(Caregory, on_delete=models.CASCADE, verbose_name='Category')
    viewed = models.IntegerField(default=0)
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
    def increase_count(self):
        self.viewed += 1
    def get_image(self):
        try:
            return self.image.url
        except:
            return 'https://cdn.iconscout.com/icon/premium/png-256-thumb/insert-image-9924441-8059276.png'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profiles', blank=True, null=True)
    def get_image(self):
        try:
            return self.photo.url
        except:
            if self.user.first_name[::-1].startswith('a'):
                return 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZy_LeJavuN0A1gksiMMkhYDcQOJ8Dqqsb1Q&s'
            else:
                return 'https://cdn.pixabay.com/photo/2020/07/01/12/58/icon-5359553_640.png'
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
class Suggestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    suggestion = models.TextField(max_length=1000, verbose_name='suggestion')

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500, verbose_name='Comment')