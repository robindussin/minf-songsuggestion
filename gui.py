import tkinter as tk
import customtkinter
from tkinter import filedialog
from tkinter import *
import os
from PIL import Image
import time
from datetime import date
import scrollableFrame
import pygame
import sys
from threading import Thread
import SliderManager
import song_suggestion


playlist_path = "/home/fpss23/gruppe04/workspace_fachprojekt/amuse-workspace/minf-songsuggestion/playlist"
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))

play_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "play-button.png")))
pause_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "pause-button.png")))

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # ------------------ Allgemeine Settings ------------------#

        self.title("2.Teilprojekt")
        self.geometry("1100x580")

        self.grid_rowconfigure(0, minsize = 65)
        self.grid_rowconfigure((1), weight=1)
        self.columnconfigure(0, weight=1)

        self.configure(fg_color="white")


        # ------------------ Frames -------------------------#

        #----------------- MenuFrame ------------------------#

        self.navigatonFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color=("white", "#2e75b5"), height=50)
        self.navigatonFrame.grid(row=0, column=0, sticky="nswe")
        self.navigatonFrame.grid_columnconfigure(0, weight=1)
        self.navigatonFrame.grid_rowconfigure(0, weight=1)

        self.guiName = customtkinter.CTkLabel(self.navigatonFrame, text="COOLER NAME", text_color=("#CB007E", "white"),
                                              font=customtkinter.CTkFont("Arial", 22, "bold"))
        self.guiName.grid(row=0, column=0, pady=5, padx=15, sticky="w")

        self.home_button = customtkinter.CTkButton(self.navigatonFrame, corner_radius=5 ,
                                                   text_color="black", hover_color="gray20",width=30, text="HOME", font= customtkinter.CTkFont("Arial", 20, "bold"),command = self.home_button_event)
        self.home_button.grid(row=0, column=1, sticky="ew",padx = 10, pady = (5,5))

        self.settings_button = customtkinter.CTkButton(self.navigatonFrame, corner_radius=5 ,
                                                       text_color="black", hover_color="gray20",width=30,text="LOG",font= customtkinter.CTkFont("Arial", 20, "bold"), command=self.settings_button_event)
        self.settings_button.grid(row=0, column=2, sticky="ew",padx = 10, pady = (5,5))

        self.notification_button = customtkinter.CTkButton(self.navigatonFrame, corner_radius=5,
                                                           text="DIRECTORIES" ,text_color="black",hover_color="gray20", font= customtkinter.CTkFont("Arial", 20, "bold"),width=30, command=self.notification_button_event)
        self.notification_button.grid(row=0, column=3, sticky="ew",padx = 10, pady = (5,5))


        #HOME
        self.homeFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="white")

        self.homeFrame.grid_rowconfigure(0, weight=1)
        self.homeFrame.columnconfigure(1, weight=1)

        # --------------- SelectionFrame ----------------#

        self.selectionFrame = customtkinter.CTkFrame(self.homeFrame, corner_radius=0, fg_color="white")
        self.selectionFrame.grid(row=0, column=0, sticky="nsew")
        # Grid-Configuration
        self.selectionFrame.grid_rowconfigure((0, 1, 2), weight=1)

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

        self.outputFrame = customtkinter.CTkFrame(self.homeFrame, corner_radius=0, fg_color="white")
        self.outputFrame.grid(row=0, column=1, sticky="nswe")

        self.outputFrame.grid_columnconfigure(0, weight=1)
        self.outputFrame.grid_rowconfigure(0, weight=1)

        self.scrollableOutput = scrollableFrame.ScrollableLabelButtonFrame(self, master=self.outputFrame, width=435,
                                                                           height=320, command=self.buttonEvent,
                                                                           corner_radius=5, fg_color="gray90")

        self.scrollableOutput.grid(row=0, column=0, padx=10, pady=10, sticky="nswe")
        self.load_songs_from_playlist({'song_paths': [], 'song_names': [], 'interprets': [], 'genres': [], 'distances': []})

        self.progressLabel = customtkinter.CTkLabel(self.outputFrame, text="Progress:", fg_color="white")
        self.progressLabel.grid(row=1, column=0, sticky="w", padx=10)

        self.progressBar = customtkinter.CTkSlider(self.outputFrame, width=765, from_=0, to=100,
                                                   command=self.slide)
        self.progressBar.grid(row=2, column=0, pady=(0, 10), sticky="w", padx=10)
        self.progressBar.set(0)

      #  self.progressTime = customtkinter.CTkLabel(self.outputFrame, text = "", fg_color="white")
       # self.progressTime.grid(row=3, column=0,pady=(0, 10), sticky="w", padx=10 )

       # self.progress = customtkinter.CTkLabel(self.outputFrame, text="0", fg_color="gray")
        #self.progress.grid(row=4, column=0, pady=(0, 10), sticky="w", padx=10)


        #LOG

        self.log = customtkinter.CTkFrame(self, fg_color="white")
        self.log.grid_columnconfigure(0, weight=1)
        self.log.grid_rowconfigure(1, weight=1)

        # Label
        self.logLabel = customtkinter.CTkLabel(self.log, height = 50, text="Log Frame",
                                               corner_radius=10, fg_color="gray90")
        self.logLabel.grid(row=0, column=0, sticky="nswe", pady=10, padx=10)

        self.logText = customtkinter.CTkTextbox(self.log, corner_radius=5,
                                                fg_color="gray90")
        self.logText.grid(row=1, column=0, padx=10, pady=10, sticky="nswe")
        self.logText.configure(state="disable")


    #DIR

        self.dir = customtkinter.CTkFrame(self, corner_radius=0, fg_color="white")

        self.dir.grid_columnconfigure(0, weight=1)
        self.dir.grid_rowconfigure(0, weight=1)

        #self.test = customtkinter.CTkButton(self, text="test", command=lambda: self.openNewWindow("Das ist ein Fehler!"))

        #self.test.grid(row=0, column = 0)

        # ----------------- Set Default Values ------------------#

        self.select_frame_by_name("home")

    # ----------------------- methods ---------------------------------#

    def open_file_dialog(self):
        self.filepath = filedialog.askopenfilename(initialdir='/media/dussin')
        filename = os.path.basename(self.filepath)
        self.musicName.configure(text="Chosen Song: " + filename)




    def StartEvent(self):
        pygame.mixer.init()
        self.length = pygame.mixer.Sound(self.filepath)
        song_length = self.length.get_length()  # Funktion zum Abrufen der Länge des Songs
        if song_length > 10 * 60:  # Überprüfung, ob die Länge länger als 8 Minuten ist (in Sekunden)
            self.musicName.configure(text="Chosen Song: ")
            error_message = "Das ausgewählte Lied ist länger als 8 Minuten!"
            self.openNewWindow(error_message)
            self.filepath = ""
        else:
            song_suggestion.start(self.filepath, self)


    def buttonEvent(self):
        print("test")

    def load_songs_from_playlist(self, songs_info):
        self.scrollableOutput.clear_list()  # Vor dem Laden der Songs entfernen wir alle vorhandenen Elemente
        for i in range(len(songs_info.get('song_paths'))):
                song_path = songs_info['song_paths'][i]
                song_name = str(i + 1) + '. ' + songs_info['song_names'][i]
                interpret = songs_info['interprets'][i]
                genre = songs_info['genres'][i]
                distance = songs_info['distances'][i]
                # print(genre, '-', song_name, '(' + interpret + ')', ':', distance)
                self.scrollableOutput.add_item(song_path, song_name, interpret, genre, distance, play_image, pause_image)

    def openNewWindow(self, text = None):

        newWindow = Toplevel()
        self.text = text
        newWindow.title("Error-Meldung")
        newWindow.geometry("200x200")


        self.Error = customtkinter.CTkLabel(newWindow,corner_radius=10, fg_color="gray90", text= text)
        self.Error.grid(row=0, column = 0, padx=20, pady = 20)

        self.agree = customtkinter.CTkButton(newWindow, fg_color="gray70", hover_color="gray20", text="Okay", command = newWindow.destroy)
        self.agree.grid(row=1, column = 0, padx = 5, pady = 5)

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.settings_button.configure(fg_color=("gray75", "gray25") if name == "settings" else "transparent")
        self.notification_button.configure(fg_color=("gray75", "gray25") if name == "notification" else "transparent")

        # show selected frame
        if name == "home":
            self.homeFrame.grid(row=1, column=0, sticky="nswe")
        else:
            self.homeFrame.grid_forget()
        if name == "settings":
            self.log.grid(row=1, column=0, sticky="nswe")
        else:
            self.log.grid_forget()
        if name == "notification":
            self.dir.grid(row=1, column=0, sticky="nswe")
        else:
            self.dir.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def settings_button_event(self):
        self.select_frame_by_name("settings")

    def notification_button_event(self):
        self.select_frame_by_name("notification")


    def slide(self,x):
        self.progress.configure(text = self.progressBar.get())


"""
    def insertLog(self, text):
        global row
        row = 0.0
        self.logText.insert(str(row),text)
        row = row + 1
"""




if __name__ == "__main__":
    app = App()
    app.mainloop()
