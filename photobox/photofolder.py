from folder import Folder


class Photofolder():

    def __init__(self, folder):
        self.folder = folder
        pass
    photoextensions = ['.jpg', '.png']

    def isint(self, str):
        try:
            int(str)
            return True
        except ValueError:
            return False

    def fileisphoto(self, file):
        extension = self.folder.getextension(file)
        return extension.lower() in self.photoextensions

    def getallphotos_filenames(self):
        return filter(lambda f: self.fileisphoto(f), self.folder.getfiles())

    def getallphotos_fullpath(self):
        return map(lambda it: self.folder.getpath() + '/' + it, self.getallphotos_filenames())

    def getphotobynumber(self, number):
        return self.folder.getpath() + "/" + self.getallphotos_filenames()[number]

    def getnextfilenumber(self):
        names = map(lambda f: self.folder.getfilename(f), self.getallphotos_filenames())
        onlynumbers = filter(lambda f: self.isint(f), names)
        numbers = map(int, onlynumbers)
        if len(numbers) == 0:
            return 1
        numbers.sort()
        return numbers[-1] + 1

    def getnextfilename_fullpath(self):
        return self.folder.getpath() + '/' + str(self.getnextfilenumber()) + '.png'

    def getlastphoto(self):
        photos = self.getallphotos_filenames()
        photos.sort()
        return photos[-1]
