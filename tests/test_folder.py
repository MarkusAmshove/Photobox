from context import photobox
from unittest import TestCase
from photobox.folder import Folder
from test_photofolder import MockFolder


class TestFolder(TestCase):
    def test_getextension_shouldreturn_thecorrectextension(self):
        folder = Folder(MockFolder([]))
        self.assertEqual(".png", folder.getextension("photo.png"))

    def test_getfilename(self):
        folder = Folder(MockFolder([]))
        self.assertEqual("photo", folder.getfilename("photo.png"))
