import pygame
import pygame_gui
import Letterboard.py
class GameManager:
    instance = None #track if Game object has been created

    #Override new so this class stays a singleton
    def __new__(cls):
        #Make a GM object if it hasn't been created already
        if cls.instrance is None:
            cls.instance = super().__new__(cls) #Record that the object was created
            #Return the new instance
            return cls.instance
    def __init__(self):
        print("Initialize game...")
        self.targetFPS = 60

        #Other variables that will be initialized when starting/running the game 
        self.screen = None
        self.isRunning = False

    def start_game(self):
        pygame.init()
        #Make the main game surface to draw stuff on
        #Getting information about the screen
        monitorDims = pygame.display.Info()
        screenWidth = monitorDims.current_w
        screenHeight = monitorDims.current_h
        self.screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)
        print("Actual:", self.screen.get_size())
        pygame.display.set_caption("Word Pathing")