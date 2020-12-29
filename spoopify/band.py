from demo.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        album_names = [a.name for a in self.albums]
        if album.name in album_names:
            return f'Band {self.name} already has {album.name} in their library.'
        self.albums.append(album)
        return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name: str):
        album_to_remove = [a for a in self.albums if a.name == album_name]
        if not album_to_remove:
            return f'Album {album_name} is not found.'
        if album_to_remove[0].published:
            return f'Album has been published. It cannot be removed.'
        self.albums.remove(album_to_remove[0])
        return f'Album {album_name} has been removed.'

    def details(self):
        band_info = f'Band {self.name}\n'
        albums_info = '\n'.join(f'{a.details()}' for a in self.albums)
        return band_info + albums_info
