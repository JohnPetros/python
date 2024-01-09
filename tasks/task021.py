# Task 21 - Write a script that opens and plays the audio from an MP3 file.

import pygame

pygame.init()

pygame.mixer.music.load('./assets/forest.mp3')

pygame.mixer.music.play()

pygame.event.wait()

