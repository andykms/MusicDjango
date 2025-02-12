from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Track, Artist, Album, Playlist, User, Genre, PlaylistTrack

# Регистрация модели Artist
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')  # Поля, отображаемые в списке
    search_fields = ('name',)  # Поля, по которым можно искать

# Регистрация модели Album
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'release_year')
    list_filter = ('artist', 'release_year')  # Фильтры справа
    search_fields = ('title', 'artist__name')  # Поиск по названию и имени исполнителя

# Регистрация модели Track
@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'album', 'duration')
    list_filter = ('artist', 'album')
    search_fields = ('title', 'artist__name', 'album__title')

# Inline-модель для редактирования треков в плейлисте
class PlaylistTrackInline(admin.TabularInline):  # Или используйте StackedInline для другого отображения
    model = PlaylistTrack
    extra = 1  # Количество пустых форм для добавления новых треков

# Регистрация модели Playlist
@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    inlines = [PlaylistTrackInline]  # Добавляем inline-форму для редактирования треков

    # Метод для отображения треков в списке плейлистов
    def get_tracks(self, obj):
        return ", ".join([track.title for track in obj.tracks.all()])
    get_tracks.short_description = 'Треки'
# Регистрация модели User (если вы используете кастомную модель пользователя)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')
    search_fields = ('username', 'email')

admin.site.register(Genre)
"""list_display: Поля, которые будут отображаться в списке объектов.

list_filter: Поля, по которым можно фильтровать объекты.

search_fields: Поля, по которым можно искать объекты.

filter_horizontal: Удобный интерфейс для выбора связанных объектов (например, треков в плейлисте).

fields или fieldsets: Управление отображением полей на странице редактирования объекта."""