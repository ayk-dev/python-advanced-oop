from math import ceil


class PhotoAlbum:
    photos_per_page = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(pages=ceil(photos_count / cls.photos_per_page))

    def add_photo(self, label:str):
        for idx, page in enumerate(self.photos):
            if len(page) < self.photos_per_page:
                page.append(label)
                page_number = idx + 1
                slot_number = len(page)
                return f'{label} photo added successfully on page {page_number} slot {slot_number}'
        return f'No more free spots'

    def display(self):
        delimiter = 11 * '-' + '\n'
        page_repr = delimiter.join([('[] ' * len(page)).rstrip() + '\n' for page in self.photos])
        album = delimiter + page_repr + delimiter
        return album