import random


class Cheesefolder():

    def __init__(self, folder):
        self.directory = folder
        pass

    def getrandomphoto(self):
        files = self.directory.getfiles_fullpath()
        filecount = len(files)
        randomindex = random.randint(0, filecount - 1)
        return files[randomindex]
