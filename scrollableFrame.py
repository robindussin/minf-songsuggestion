import customtkinter
from PIL import Image
import os
import pygame




class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):

    current_dir = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.label_list = []
        self.button_list = []

    def add_item(self, image_play=None, image_pause=None):
        label = customtkinter.CTkLabel(self, text="music_path",padx=5, anchor="w")

        play_button = customtkinter.CTkButton(self,text="", image=image_play)
        pause_button = customtkinter.CTkButton(self, text="", image=image_pause)

        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        play_button.grid(row=int(len(self.button_list)/2), column=1, pady=(0, 10), padx=5)
        pause_button.grid(row=int(len(self.button_list)/2), column=2, pady=(0, 10), padx=5)

        self.label_list.append(label)
        self.button_list.append(play_button)
        self.button_list.append(pause_button)

    def remove_item(self, item):
        for label, button in zip(self.label_list, self.button_list):
            if item == label.cget("text"):
                label.destroy()
                button.destroy()
                self.label_list.remove(label)
                self.button_list.remove(button)
                return

    def play_song(self, idx):
        pygame.mixer.init()
        pygame.mixer.music.load(f"song_{idx + 1}.mp3")
        pygame.mixer.music.play()

    def pause_song(self, idx):
        pygame.mixer.music.pause()
