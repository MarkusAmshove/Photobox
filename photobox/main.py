import pygame
import time
import os
import Colors
from photoslideshow import Photoslideshow


class Photobox():

    def __init__(self, windowsize, photofolder, camera):
        pygame.init()
        self.windowsize = windowsize
        self.photofolder = photofolder
        self.screen = pygame.display.set_mode(self.windowsize, pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.camera = camera
        pygame.mouse.set_visible(0)

    def start(self):
        slideshow = Photoslideshow(self)
        while True:
            self.clearscreen()
            slideshow.shownextphoto()
            self.handleevents()
            time.sleep(2)

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
        events = pygame.event.get()
        if len(events) == 0:
            return
        event = events[0]
        if event.type == pygame.KEYDOWN:
            self.handlekeyevent(event.key)
        pygame.event.clear()

    def handlekeyevent(self, key):
        if key == pygame.K_ESCAPE:
            os.system("sudo shutdown now -h")
            exit(0)
        if key == pygame.K_RETURN:
            self.takenewphoto()
        if key == pygame.K_F4:
            exit(1)

    def takenewphoto(self):
        start = time.clock()
        self.showcountdown(3)
        stop = time.clock()
        print("Showing Countdown took " + str(stop - start) + " seconds")
        self.showtext("Cheese!", 400)
        start = time.clock()
        nextphotophath = self.photofolder.getnextfilename_fullpath()
        stop = time.clock()
        print("Getting next filepath took " + str(stop - start) + " seconds")
        start = time.clock()
        photoTaken = self.camera.takephoto(nextphotophath)
        stop = time.clock()
        print("Taking the photo took " + str(stop - start) + " seconds")
        if photoTaken:
            self.showphoto(nextphotophath)

    def showcountdown(self, upperbound):
        for i in range(upperbound, 0, -1):
            self.showtext(str(i), 400)
            time.sleep(1)