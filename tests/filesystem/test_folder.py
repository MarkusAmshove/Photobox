from unittest import TestCase
from photobox.filesystem.folder import Folder
from tests.core.test_photofolder import MockFolder


class TestFolder(TestCase):
    def test_getextension_shouldreturn_thecorrectextension(self):
        folder = Folder(MockFolder([]))
        self.assertEqual(".png", folder.getextension("photo.png"))

    def test_getfilename(self):
        folder = Folder(MockFolder([]))
        self.assertEqual("photo", folder.getfilename("photo.png"))
