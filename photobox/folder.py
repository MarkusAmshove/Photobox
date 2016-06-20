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

    def getfiles_fullpath(self):
        files = self.getfiles()
        return map(lambda it: os.path.join(self.getpath(), it), files)


class RealFolder(Folder):
    def getfiles(self):
        return os.listdir(self.getpath())
