import customtkinter
from PIL import Image
import os
import pygame
import SliderManager
import time




class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):

    current_dir = os.path.dirname(os.path.abspath(__file__))


    def __init__(self,app, master, command=None, **kwargs ):
        super().__init__(master, **kwargs)
        self.app = app
        self.grid_columnconfigure(0, weight=1)
        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.label_list = []
        self.button_list = []

    def add_item(self, music_path, filename, interpret, genre, distance, image_play=None, image_pause=None):
        label_text = filename + ' - ' + interpret + ' (' + genre + '): ' + str(distance)
        musicLabel = customtkinter.CTkLabel(self, text=label_text,padx=5, anchor="w")

        play_button = customtkinter.CTkButton(self, width=15, text="",fg_color="gray70",hover_color="gray20", image=image_play, command=lambda idx=len(self.label_list) - 1: self.play_song(music_path))
        pause_button = customtkinter.CTkButton(self, width=15, text="",fg_color="gray70", hover_color="gray20", image=image_pause, command=lambda idx=len(self.label_list) - 1: self.pause_song(music_path))

        musicLabel.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        play_button.grid(row=int(len(self.button_list)/2), column=1, pady=(0, 10), padx=5)
        pause_button.grid(row=int(len(self.button_list)/2), column=2, pady=(0, 10), padx=5)

        self.label_list.append(musicLabel)
        self.button_list.append(play_button)
        self.button_list.append(pause_button)

    def remove_item(self, item):
        for label, play_button, pause_button in zip(self.label_list, self.play_button_list, self.pause_button_list):
            if item == label.cget("text"):
                label.destroy()
                play_button.destroy()
                pause_button.destroy()
                self.label_list.remove(label)
                self.play_button_list.remove(play_button)
                self.pause_button_list.remove(pause_button)
                return

    def clear_list(self):
        self.label_list = []
        self.button_list = []

    def play_song(self, idx):
        print(idx)
        pygame.mixer.init()  # Konvertiere idx + 1 in einen String
        self.sound = pygame.mixer.Sound(idx)
        pygame.mixer.music.load(idx)
        pygame.mixer.music.play()
        self.play_time()
        slider_position = int(self.sound.get_length())
        self.app.progressBar.configure(to=slider_position)


    def pause_song(self, idx):
        pygame.mixer.music.pause()


    def updateSong(self, value, filepath):
        pygame.mixer_music.set_pos(value * self.sound.get_length() / 100)


    def play_time(self):
        current_time = pygame.mixer.music.get_pos() / 1000



        converted_time = time.strftime("%M:%S", time.gmtime(current_time))


        song_length = self.sound.get_length()

        converted_song_length = time.strftime("%M:%S", time.gmtime(song_length))



        self.app.progressBar.set(int(current_time))

        self.app.progressBar.after(1000, self.play_time)

    def slide(self,x):
        pass





