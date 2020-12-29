from demo.song import Song


class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."

        song_names = [s.name for s in self.songs]
        if song.name in song_names:
            return f"Song is already in the album."

        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str):
        if self.published:
            return 'Cannot remove songs. Album is published.'
        song_to_remove = [s for s in self.songs if s.name == song_name]
        if not song_to_remove:
            return "Song is not in the album."
        self.songs.remove(song_to_remove[0])
        return f'Removed song {song_name} from album {self.name}.'

    def publish(self):
        if self.published:
            return f'Album {self.name} is already published.'
        self.published = True
        return f'Album {self.name} has been published.'

    def details(self):
        album_name = f'Album {self.name}\n'
        songs_info = '\n'.join(f'== {s.name} - {s.length}' for s in self.songs)
        return album_name + songs_info





