import random


class Photoslideshow():
    def __init__(self, photobox):
        self.photobox = photobox
        self.nextPhotoNumber = 1
        self.lastRandomIndex = -1

    def shownextphoto(self):
        self.shownextphoto_byorder()

    def shownextphoto_random(self):
        photos = self.photobox.photofolder.getallphotos_fullpath()
        randomindex = random.randint(0, len(photos) - 1)
        while randomindex == self.lastRandomIndex and len(photos) not in range(0, 2):
            randomindex = random.randint(0, len(photos) - 1)
        self.lastRandomIndex = randomindex
        self.photobox.showphoto(photos[randomindex])

    def shownextphoto_byorder(self):
        self.nextPhotoNumber %= len(self.photobox.photofolder.getallphotos_filenames())
        nextPhoto = self.photobox.photofolder.getphotobynumber(self.nextPhotoNumber)
        self.photobox.showphoto(nextPhoto)
        self.nextPhotoNumber += 1
