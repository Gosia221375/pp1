class Pieces_of_music():
    def __init__(self, artist, track_title, album, year):
        self.artist = artist
        self.track_title = track_title
        self.album = album
        self.year = year

    def __str__(self):
        return f"Performer: {self.artist}\nSong: {self.track_title}\n Album: {self.album}\n Year: {self.year}"

music1 = Pieces_of_music("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", "2017")
music2 = Pieces_of_music("Michael Jackson", "Beat It", "Thriller", "1983")
music3 = Pieces_of_music("Queen", "Bohemian Rhapsody", "Album", "1975")
print(music1)
print(music2)
print(music3)