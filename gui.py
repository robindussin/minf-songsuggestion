import tkinter

import customtkinter
from tkinter import filedialog
import os
from PIL import Image
import time
from datetime import date
import scrollableFrame
import pygame

import song_suggestion

playlist_path = "C:/Studium/Fachprojekt/2.Teilprojekt/minf-songsuggestion/playlist"
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))

play_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "play-button.png")))
pause_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "pause-button.png")))

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # ------------------ Allgemeine Settings ------------------#

        self.title("2.Teilprojekt")
        self.geometry("800x400")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.configure(fg_color="white")

        # ------------------ Frames -------------------------#

        # --------------- SelectionFrame ----------------#

        self.selectionFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="white")
        self.selectionFrame.grid(row=0, column=0, sticky="nsew")
        # Grid-Configuration
        self.selectionFrame.grid_rowconfigure((0, 1), weight=1)
        self.selectionFrame.grid_rowconfigure(2, weight=1)
        self.selectionFrame.grid_columnconfigure(1, weight=1)

        # Label
        self.selectionLabel = customtkinter.CTkLabel(self.selectionFrame, width=300, text="Choose your Song!",
                                                     corner_radius=10, fg_color="gray90")
        self.selectionLabel.grid(row=0, column=0, columnspan=2, sticky="nswe", pady=10, padx=10)

        self.musicName = customtkinter.CTkLabel(self.selectionFrame, text="Chosen Song: ", corner_radius=10,
                                                fg_color="gray90")
        self.musicName.grid(row=2, column=0, columnspan=2, sticky="nswe", pady=10, padx=10)

        # Button
        self.selectionButton = customtkinter.CTkButton(self.selectionFrame, text="Select!", text_color="black",
                                                       fg_color="transparent", hover_color="gray80",
                                                       command=self.open_file_dialog)
        self.selectionButton.grid(row=1, column=0, sticky="ns", pady=10, padx=10)

        self.startButton = customtkinter.CTkButton(self.selectionFrame, text="Start!", text_color="black",
                                                   fg_color="transparent", hover_color="gray80",
                                                   command=self.StartEvent)
        self.startButton.grid(row=1, column=1, sticky="ns", pady=10, padx=10)

        self.playButton = customtkinter.CTkButton(self.selectionFrame, text="",fg_color="gray70",hover_color="gray20", image=play_image,  command=lambda: self.scrollableOutput.play_song(self.filepath))
        self.playButton.grid(row=3, column=0, pady=(0,10), padx=10, sticky="w")

        self.pauseButton = customtkinter.CTkButton(self.selectionFrame, text="", fg_color="gray70", hover_color="gray20", image=pause_image, command=lambda: self.scrollableOutput.pause_song(self.filepath))
        self.pauseButton.grid(row=3, column=1, pady=(0,10),padx=10, sticky="w")

        # --------------- OutputFrame ----------------#

        self.outputFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="white")
        self.outputFrame.grid(row=0, column=1, sticky="nswe")

        self.scrollableOutput = scrollableFrame.ScrollableLabelButtonFrame(master=self.outputFrame, width=435,
                                                                           height=320, command=self.buttonEvent,
                                                                           corner_radius=5, fg_color="gray90")
        self.scrollableOutput.grid(row=0, column=1, padx=10, pady=10, sticky="nswe")
        self.load_songs_from_playlist(play_image, pause_image)

        self.progressLabel = customtkinter.CTkLabel(self.outputFrame, text="Progress:", fg_color="white")
        self.progressLabel.grid(row=1, column=1, sticky="w", padx=10)

        self.progressBar =customtkinter.CTkProgressBar(self.outputFrame, width=435, mode="determinate")
        self.progressBar.grid(row=2, column=1, sticky="w", padx=10)

    # ----------------------- methods ---------------------------------#

    def open_file_dialog(self):
        self.filepath = filedialog.askopenfilename(initialdir='/home/dussin/Downloads')
        filename = os.path.basename(self.filepath)
        self.musicName.configure(text="Chosen Song: " + filename)

    def StartEvent(self):
        song_suggestion.start(self.filepath)

    def buttonEvent(self):
        print("test")

    def load_songs_from_playlist(self, play_image, pause_image):
        # self.scrollableOutput.clear_items()  # Vor dem Laden der Songs entfernen wir alle vorhandenen Elemente
        for filename in os.listdir(playlist_path):
            if filename.endswith(".mp3"):
                music_path = os.path.join(playlist_path, filename)
                print(filename)
                self.scrollableOutput.add_item(music_path, image_play=play_image, image_pause=pause_image)




if __name__ == "__main__":
    app = App()
    app.mainloop()
