from context import photobox
from unittest import TestCase
from photobox.photofolder import Photofolder
from photobox.folder import Folder


class MockFolder(Folder):

    def __init__(self, files, path=""):
        self.files = files
        self.path = path

    def getfiles(self):
        return self.files


class TestPhotofolder(TestCase):
    def test_fileisphoto_withpng(self):
        photofolder = Photofolder(MockFolder([]))
        self.assertTrue(photofolder.fileisphoto("photo.png"))

    def test_fileisphoto_withjpg(self):
        photofolder = Photofolder(MockFolder([]))
        self.assertTrue(photofolder.fileisphoto("photo.jpg"))

    def test_fileisphoto_withtxt(self):
        photofolder = Photofolder(MockFolder([]))
        self.assertFalse(photofolder.fileisphoto("nophoto.txt"))

    def test_getallphotos_shouldreturn_thephotos(self):
        photofolder = Photofolder(MockFolder(["photo1.jpg"]))
        self.assertListEqual(["photo1.jpg"], photofolder.getallphotos_filenames())

    def test_getallphotos_shouldnotreturn_fileswhicharentphotos(self):
        photofolder = Photofolder(MockFolder(["1.jpg", "2.png", "nophoto.txt"]))
        self.assertListEqual(["1.jpg", "2.png"], photofolder.getallphotos_filenames())

    def test_getnextfilenumber_shouldreturn_thenextfilename(self):
        photofolder = Photofolder(MockFolder(["2.png", "1.jpg"]))
        self.assertEqual(3, photofolder.getnextfilenumber())

    def test_getnextfilenumber_shouldreturn_1whenwrongconvention(self):
        photofolder = Photofolder(MockFolder(["photo.jpg"]))
        self.assertEqual(1, photofolder.getnextfilenumber())

    def test_getnextfilenumber_shouldreturn_1whennophoto(self):
        photofolder = Photofolder(MockFolder([]))
        self.assertEqual(1, photofolder.getnextfilenumber())

    def test_getlastphoto_shouldreturn_thelastphoto(self):
        photofolder = Photofolder(MockFolder(["2.png", "1.png"]))
        self.assertEqual("2.png", photofolder.getlastphoto())

    def test_getnextfilenumber_fullpath_shouldreturn_thefullpath(self):
        photofolder = Photofolder(MockFolder(["2.png", "1.png"], "home"))
        self.assertEqual("home/3.png", photofolder.getnextfilename_fullpath())
