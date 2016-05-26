import subprocess
import core.camera
from subprocess import Popen, PIPE


class Gphoto():
    def takephoto(self, path):
        return subprocess.call(
            [
                 "gphoto2", "--capture-image-and-download", "--filename", path
            ]) == 0
