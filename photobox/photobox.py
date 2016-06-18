from photofolder import Photofolder
from folder import RealFolder
from gphotocamera import Gphoto
from main import Photobox
from rcswitch import RCSwitch

##########
# config #
##########
photodirectory = '/var/www/html/'
windowwidth = 1024
windowheight = 768
camera = Gphoto()
switch = RCSwitch(2352753, 2352754, "NOT_IMPLEMENTED")
##########
filesystemFolder = RealFolder(photodirectory)
photofolder = Photofolder(filesystemFolder)
photobox = Photobox((windowwidth, windowheight), photofolder, camera, switch)
photobox.start()
