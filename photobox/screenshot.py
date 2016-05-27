from subprocess import Popen, PIPE
import core.camera


class ScreenshotCamera():
    def takephoto(self, path):
        proc = Popen(['scrot', path])
