class Track:
    def __init__(self, name, duration=0):
        self.name = name
        self.duration = int(duration)

    def __str__(self):
        return f'{self.name}-{self.duration}sec'

    def __lt__(self, other):
        if not isinstance(other, Track):
            print('Это не класс Track')
        return self.duration < other.duration

class Album:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.list_track = []

    def get_tracks(self):
        if not self.list_track:
            print('В этом альбоме пока нет треков')
        else:
            for track in self.list_track:
                return track

    def add_track(self, track):
       if track in self.list_track:
           print('Такой трек уже есть')
       else:
           self.list_track.append(track)

    def get_duration(self):
        if not self.list_track:
            print('В этом альбоме пока нет треков')
        else:
            sum_tracks_duration = 0
            for track in self.list_track:
                sum_tracks_duration += track.duration
            print(sum_tracks_duration)

    def __str__(self):
        A = f'Name group: {self.group}\nName album: {self.name}\nTracks:\n	'
        B = f'\n	'.join([track.__str__() for track in self.list_track])
        return A+B


misery = Track('Misery', 180)
anna = Track('Anna', 167)
little_child = Track('Little Child', 192)

please_please_me = Album('Please Please Me', 'The Beatles')
please_please_me.list_track = [misery, anna]

with_the_beatles = Album('With the Beatles', 'The Beatles')
with_the_beatles.list_track = [little_child]



print(please_please_me)
print()
print(with_the_beatles)
print()
print(misery > little_child)