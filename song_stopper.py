import pygame
import random
import time


pygame.mixer.init()

def play_musical_chairs():
    print("Welcome to Musical Chairs!")

    song_path = input("Enter the file path to the local audio file: ")

    try:
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()

        print(" Music is playing! ")

       
        stop_time = random.randint(10, 60)
        print(f"The music will pause randomly within x seconds!")

        
        time.sleep(stop_time)

        pygame.mixer.music.stop()
        print("\n Music has paused! Grab a chair! ")

    except pygame.error as e:
        print(f"Error loading or playing the music: {e}")

play_musical_chairs()
