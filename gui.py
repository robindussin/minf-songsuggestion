<<<<<<< HEAD
import tkinter
=======
>>>>>>> 6e0b7f78f651b2d71a810fd0e6c0dd941133a249
import customtkinter
from tkinter import filedialog
import os
from PIL import Image
from time import strftime
from datetime import date
import scrollableFrame
<<<<<<< HEAD
import pygame
=======
import song_suggestion
>>>>>>> 6e0b7f78f651b2d71a810fd0e6c0dd941133a249



playlist_path = "C:/Studium/Fachprojekt/2.Teilprojekt/minf-songsuggestion/playlist"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

<<<<<<< HEAD


    #------------------ Allgemeine Settings ------------------#
=======
        #------------------ Allgemeine Settings ------------------#
>>>>>>> 6e0b7f78f651b2d71a810fd0e6c0dd941133a249

        self.title("2.Teilprojekt")
        self.geometry("800x400")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.configure(fg_color="white")




        #------------------ Frames -------------------------#


        #--------------- SelectionFrame ----------------#

        self.selectionFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="white")
        self.selectionFrame.grid(row=0, column=0, sticky="nsew")
        #Grid-Configuration
        self.selectionFrame.grid_rowconfigure((0,1), weight=1)
        self.selectionFrame.grid_rowconfigure(2, weight=1)



        #Label
        self.selectionLabel = customtkinter.CTkLabel(self.selectionFrame,width=300,text="Choose your Song!", corner_radius=10, fg_color="gray90")
        self.selectionLabel.grid(row=0,column=0, sticky="nswe", pady=10, padx=10)

        #Button
        self.selectionButton = customtkinter.CTkButton(self.selectionFrame,width=300, text="Select!",text_color="black", fg_color="transparent", hover_color="gray80", command=self.open_file_dialog)
        self.selectionButton.grid(row=1,column=0, sticky="nswe", pady=10, padx=10)

        self.startButton = customtkinter.CTkButton(self.selectionFrame,width=300, text="Start!",text_color="black", fg_color="transparent", hover_color="gray80", command=self.buttonEvent)
        self.startButton.grid(row=2, column=0, sticky="nswe", pady=10, padx=10)



        # --------------- OutputFrame ----------------#

        self.outputFrame = customtkinter.CTkFrame(self, corner_radius=0,fg_color="white")
        self.outputFrame.grid(row=0, column=1, sticky="nswe")


        self.scrollableOutput = scrollableFrame.ScrollableLabelButtonFrame(master = self.outputFrame,width=435,height=360, command=self.buttonEvent, corner_radius=5, fg_color="gray90")
        self.scrollableOutput.grid(row=0, column=1, padx=10, pady=10, sticky="nswe")

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
        for i in range(10):  # add items with images
           self.scrollableOutput.add_item(image_play=customtkinter.CTkImage(Image.open(os.path.join(image_path, "play-button.png"))), image_pause=customtkinter.CTkImage(Image.open(os.path.join(image_path, "pause-button.png"))))



#----------------------- methods ---------------------------------#

    def open_file_dialog(self):
<<<<<<< HEAD
        file_path = tkinter.filedialog.askopenfilename()
        tkinter.path_entry.delete(0, tkinter.END)
        tkinter.path_entry.insert(tkinter.END, file_path)
=======
        self.file_path = filedialog.askopenfilename(initialdir = '/home/dussin/Downloads')
>>>>>>> 6e0b7f78f651b2d71a810fd0e6c0dd941133a249

    def buttonEvent(self):
        song_suggestion.start(self.file_path)





if __name__ == "__main__":
    app = App()
    app.mainloop()
