from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Модель пользователя (расширяем стандартную модель User)
class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='artists/', blank=True, null=True) 
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='striming_user_set',  # Уникальное имя для обратной связи
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='striming_user_set',  # Уникальное имя для обратной связи
        related_query_name='user',
    ) 

# Модель исполнителя
class Artist(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    photo_url = models.ImageField(upload_to='artists/', blank=True, null=True)  # Поле для загрузки фото

    def __str__(self):
        return self.name

class Genre(models.Model):
    gerne_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.gerne_name


# Модель альбома
class Album(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    cover_url = models.ImageField(upload_to='albums/', blank=True, null=True)  # Поле для загрузки фото
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')

    def __str__(self):
        return self.title

# Модель трека
class Track(models.Model):
    title = models.CharField(max_length=255)
    duration = models.FloatField()  # Длительность в секундах
    file_url = models.FileField(upload_to='tracks/', blank=True, null=True) # Ссылка на аудиофайл
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='tracks')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Жанр")
    def __str__(self):
        return self.title

# Модель плейлиста
class Playlist(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    tracks = models.ManyToManyField(Track, through='PlaylistTrack')

    def __str__(self):
        return self.title

# Промежуточная модель для связи плейлистов и треков (с порядком треков)
class PlaylistTrack(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    order = models.IntegerField()  # Порядок трека в плейлисте

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.playlist.title} - {self.track.title} (Order: {self.order})"
    

