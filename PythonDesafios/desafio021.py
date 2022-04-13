import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('classic_rock.mp3')
pygame.mixer.music.play()
pygame.event.wait()

