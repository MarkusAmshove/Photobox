from os.path import expanduser

from core.photofolders import Photofolder
from filesystem.folder import RealFolder
from core.gphotocamera import Gphoto
from core.photofolders import Photofolder
from ui.main import Photobox


# from photobox.core.photofolder import Photofolder
# from photobox.filesystem.folder import RealFolder
# from photobox.core.gphotocamera import Gphoto
# from photobox.ui.main import Photobox

##########
# config #
##########
# photodirectory = expanduser('~/photobox')
photodirectory = '/var/www/html/'
windowwidth = 1024
windowheight = 768
camera = Gphoto()
##########
filesystemFolder = RealFolder(photodirectory)
photofolder = Photofolder(filesystemFolder)
photobox = Photobox((windowwidth, windowheight), photofolder, camera)
photobox.start()
