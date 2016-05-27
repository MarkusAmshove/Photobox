from os.path import expanduser

from photofolder import Photofolder
from folder import RealFolder
from gphotocamera import Gphoto
from main import Photobox

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
