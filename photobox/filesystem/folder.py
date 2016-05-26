import os


class Folder():
    def __init__(self, path):
        self.path = path
        pass

    def getfiles(self):
        raise NotImplementedError()

    def getpath(self):
        return self.path

    def getfileinfo(self, thefile):
        return os.path.splitext(thefile)

    def getextension(self, thefile):
        filename, fileextension = self.getfileinfo(thefile)
        return fileextension

    def getfilename(self, thefile):
        filename, fileextension = self.getfileinfo(thefile)
        return filename


class RealFolder(Folder):
    def getfiles(self):
        return os.listdir(self.getpath())
