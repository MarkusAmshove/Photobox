import pygame
import time
import datetime
import os
import Colors
import SwitchState
from photoslideshow import Photoslideshow


class Photobox():

    def __init__(self, windowsize, photofolder, camera, switch):
        pygame.init()
        self.windowsize = windowsize
        self.photofolder = photofolder
        self.screen = pygame.display.set_mode(
            self.windowsize, pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.camera = camera
        self.switch = switch
        self.countdowntime = 3
        self.estimatedtriggertime = 2
        self.lastphototaken = datetime.datetime.now()
        pygame.mouse.set_visible(0)

    def start(self):
        slideshow = Photoslideshow(self)
        self.slideshow = slideshow
        while True:
            # don't crash the program if an error happens
            try:
                self.clearscreen()
                slideshow.shownextphoto()
                self.handleevents()
                self.exit_if_needed()
            except:
                pass

    def exit_if_needed(self):
        events = pygame.event.get()
        if len(events) == 0:
            return
        event = events[0]
        if event.type == pygame.KEYDOWN:
            key = event.key
            if key == pygame.K_ESCAPE:
                exit()

    def showphoto(self, path):
        self.clearscreen()
        photo = pygame.image.load(path)
        photo = pygame.transform.scale(photo, self.windowsize)
        self.screen.blit(photo, (0, 0))
        self.updatescreen()

    def updatescreen(self):
        pygame.display.flip()

    def clearscreen(self):
        self.screen.fill((0, 0, 0))

    def showtext(self, text, fontsize):
        self.clearscreen()
        font = pygame.font.Font(None, fontsize)
        fontWidth = font.size(text)[0]
        fontHeight = font.size(text)[1]
        midX = self.windowsize[0] / 2 - fontWidth / 2
        midY = self.windowsize[1] / 2 - fontHeight / 2
        screentext = font.render(text, True, Colors.randomcolor_rgb())
        self.screen.blit(screentext, (midX, midY))
        self.updatescreen()

    def handleevents(self):
        switchstate = self.switch.get_switch_state()
        if switchstate == SwitchState.SHUTDOWN:
            os.system("sudo shutdown now -h")
            exit(0)
        if switchstate == SwitchState.EXIT:
            exit(0)
        if self.newPhotoAllowed:
            if switchstate == SwitchState.TRIGGER:
                self.lastphototaken = datetime.datetime.now()
                self.takenewphoto()
                self.slideshow.reset_timer()

    def newPhotoAllowed(self):
        secondsdelta = self.countdowntime + self.estimatedtriggertime + 3
        nextphotoallowed = (self.lastphototaken +
                            datetime.timedelta(0, secondsdelta))
        timenow = datetime.datetime.now()
        if timenow > nextphotoallowed:
            return True
        return False

    def takenewphoto(self):
        self.showcountdown(self.countdowntime)
        self.showtext("Cheese!", 300)
        nextphotophath = self.photofolder.getnextfilename_fullpath()
        photoTaken = self.camera.takephoto(nextphotophath)
        if photoTaken:
            self.showphoto(nextphotophath)

    def showcountdown(self, upperbound):
        for i in range(upperbound, 0, -1):
            self.showtext(str(i), 400)
            time.sleep(1)
