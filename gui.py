import tkinter as tk
import customtkinter
import os
from PIL import Image
from time import strftime
from datetime import date
import scrollableFrame


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

    #------------------ Allgemeine Settings ------------------#

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


#----------------------- methods ---------------------------------#

    def open_file_dialog(self):
        file_path = customtkinter.filedialog.askopenfilename()
        customtkinter.path_entry.delete(0, tk.END)
        customtkinter.path_entry.insert(tk.END, file_path)

    def buttonEvent(self):
        print("Pressed Button")



if __name__ == "__main__":
    app = App()
    app.mainloop()